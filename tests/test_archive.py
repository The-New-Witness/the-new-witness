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

    def test_existing_project_archive(self):
        self.assertGreater(validate(Path(__file__).resolve().parents[1] / 'the-new-witness-full.zip'), 0)

    def test_missing_required_file(self):
        with self.assertRaisesRegex(ValueError, 'Missing required'):
            validate(self.fixture(['README.md']))

    def test_parent_traversal(self):
        with self.assertRaisesRegex(ValueError, 'Unsafe archive path'):
            validate(self.fixture(['../outside']), required=set())

    def test_absolute_or_windows_path(self):
        for name in ['/outside', 'C:/outside', 'folder\\outside']:
            with self.subTest(name=name), self.assertRaisesRegex(ValueError, 'Unsafe archive path'):
                validate(self.fixture([name]), required=set())

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
