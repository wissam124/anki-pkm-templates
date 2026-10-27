from __future__ import annotations

import re
import shutil
import subprocess
import tempfile
import unittest
from pathlib import Path

import generate


class GeneratedOutputTests(unittest.TestCase):
    def setUp(self) -> None:
        self.generated = generate.outputs()

    def test_generated_outputs_validate(self) -> None:
        self.assertEqual(generate.validate(self.generated), [])

    def test_each_source_template_has_one_enhancement_placeholder(self) -> None:
        for source_name in generate.TEMPLATES.values():
            source = generate.read(generate.SOURCE / "templates" / source_name)
            self.assertEqual(source.count("<!-- @enhance -->"), 1, source_name)

    def test_generated_artifacts_identify_themselves(self) -> None:
        build_ids = set()
        for path, content in self.generated.items():
            self.assertIn(f"PKM SJ artifact: {path.name}", content)
            match = re.search(r"build: ([0-9a-f]{12})", content[:512])
            self.assertIsNotNone(match, path)
            build_ids.add(match.group(1))
        self.assertEqual(len(build_ids), 1)

    def test_only_marked_files_are_generator_owned(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            personal = root / "notes.txt"
            managed = root / "old-output.css"
            personal.write_text("personal notes\n", encoding="utf-8")
            managed.write_text(generate.GENERATED_MARKER, encoding="utf-8")
            self.assertFalse(generate.is_managed_output(personal))
            self.assertTrue(generate.is_managed_output(managed))

    @unittest.skipUnless(shutil.which("node"), "Node.js is needed for JS syntax checks")
    def test_generated_javascript_parses(self) -> None:
        for path, content in self.generated.items():
            if path.suffix != ".html":
                continue
            script = content.split("<script>", 1)[1].split("</script>", 1)[0]
            with tempfile.NamedTemporaryFile("w", suffix=".js", encoding="utf-8") as handle:
                handle.write(script)
                handle.flush()
                result = subprocess.run(
                    ["node", "--check", handle.name],
                    capture_output=True,
                    text=True,
                    check=False,
                )
            self.assertEqual(result.returncode, 0, f"{path}: {result.stderr}")


if __name__ == "__main__":
    unittest.main()
