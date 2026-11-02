"""Validate the distributed archive without extracting or executing its contents."""
from pathlib import Path, PurePosixPath
import stat
import sys
import zipfile

REQUIRED = {
    'README.md', 'LICENSE', 'frontend/tracker/index.js',
    'frontend/emotional-visualizer/index.js', 'frontend/deprogrammer/index.js',
    'frontend/shared/styles.css', 'deploy/replit.sh',
}


def validate(path, required=REQUIRED):
    with zipfile.ZipFile(path) as archive:
        seen = set()
        for entry in archive.infolist():
            name = entry.filename
            parts = PurePosixPath(name).parts
            if not name or name.startswith('/') or '\\' in name or ':' in name or '..' in parts:
                raise ValueError(f'Unsafe archive path: {name!r}')
            if name in seen:
                raise ValueError(f'Duplicate archive path: {name!r}')
            if stat.S_ISLNK(entry.external_attr >> 16):
                raise ValueError(f'Archive symlink is not supported: {name!r}')
            if entry.flag_bits & 1:
                raise ValueError('Encrypted entries cannot be integrity-checked')
            seen.add(name)
        missing = required - seen
        if missing:
            raise ValueError(f'Missing required archive files: {sorted(missing)}')
        corrupt = archive.testzip()
        if corrupt:
            raise ValueError(f'CRC verification failed: {corrupt!r}')
    return len(seen)


if __name__ == '__main__':
    target = Path(__file__).resolve().parents[1] / 'the-new-witness-full.zip'
    try:
        count = validate(target)
    except (ValueError, OSError, zipfile.BadZipFile) as error:
        print(f'Archive validation failed: {error}', file=sys.stderr)
        raise SystemExit(1) from None
    print(f'Archive integrity verified: {count} entries. Contents were not extracted or executed.')
