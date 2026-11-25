from pathlib import Path
import stat
import tempfile
import unittest
import warnings
import zipfile

from scripts.validate_archive import validate


class ArchiveTests(unittest.TestCase):
    def fixture(self, names):
        tmp = tempfile.TemporaryDirectory()
        self.addCleanup(tmp.cleanup)
        path = Path(tmp.name) / 'archive.zip'
        with warnings.catch_warnings(), zipfile.ZipFile(path, 'w') as archive:
            warnings.simplefilter('ignore', UserWarning)
            for name in names:
                archive.writestr(name, 'content')
        return path

    def fixture_raw_path(self, raw_name):
        # ZipInfo normalizes backslashes when constructing a fixture on Windows.
        # Replace both ZIP header names after writing to preserve the raw bytes.
        safe = b'folder/outside'
        self.assertEqual(len(safe), len(raw_name))
        path = self.fixture([safe.decode('ascii')])
        data = path.read_bytes()
        self.assertEqual(data.count(safe), 2)
        path.write_bytes(data.replace(safe, raw_name))
        with zipfile.ZipFile(path) as archive:
            self.assertEqual(archive.infolist()[0].orig_filename, raw_name.decode('ascii'))
        return path

    def test_existing_project_archive(self):
        self.assertGreater(validate(Path(__file__).resolve().parents[1] / 'the-new-witness-full.zip'), 0)

    def test_missing_required_file(self):
        with self.assertRaisesRegex(ValueError, 'Missing required'):
            validate(self.fixture(['README.md']))

    def test_parent_traversal(self):
        with self.assertRaisesRegex(ValueError, 'Unsafe archive path'):
            validate(self.fixture(['../outside']), required=set())

    def test_absolute_or_windows_path(self):
        for name in ['/outside', 'C:/outside']:
            with self.subTest(name=name), self.assertRaisesRegex(ValueError, 'Unsafe archive path'):
                validate(self.fixture([name]), required=set())

    def test_raw_windows_separator(self):
        with self.assertRaisesRegex(ValueError, 'Unsafe archive path'):
            validate(self.fixture_raw_path(b'folder\\outside'), required=set())

    def test_raw_nul(self):
        with self.assertRaisesRegex(ValueError, 'Unsafe archive path'):
            validate(self.fixture_raw_path(b'folder\x00outside'), required=set())

    def test_duplicate_path(self):
        with self.assertRaisesRegex(ValueError, 'Duplicate archive path'):
            validate(self.fixture(['README.md', 'README.md']), required=set())

    def test_symlink(self):
        path = self.fixture([])
        entry = zipfile.ZipInfo('link')
        entry.create_system = 3
        entry.external_attr = (stat.S_IFLNK | 0o777) << 16
        with zipfile.ZipFile(path, 'a') as archive:
            archive.writestr(entry, '../outside')
        with self.assertRaisesRegex(ValueError, 'symlink'):
            validate(path, required=set())


if __name__ == '__main__':
    unittest.main()
