"""Check the bundled plugin files and marketplace without network or dependencies."""
from __future__ import annotations

import hashlib
import json
from pathlib import Path
import sys


def verify(root: Path) -> list[str]:
    lock = json.loads((root / 'plugins.lock.json').read_text(encoding='utf-8'))
    marketplace = json.loads(
        (root / '.claude-plugin/marketplace.json').read_text(encoding='utf-8')
    )
    errors: list[str] = []
    expected = set(lock['files'])
    actual = {
        path.relative_to(root).as_posix()
        for path in (root / 'plugins').rglob('*')
        if path.is_file() and '__pycache__' not in path.parts and path.suffix != '.pyc'
    }
    errors.extend(f'Missing file: {name}' for name in sorted(expected - actual))
    errors.extend(f'Untracked plugin file: {name}' for name in sorted(actual - expected))
    for name in sorted(expected & actual):
        digest = hashlib.sha256((root / name).read_bytes()).hexdigest()
        if digest != lock['files'][name]['sha256']:
            errors.append(f'Checksum mismatch: {name}')

    aliases = lock.get('install_aliases', {})
    expected_names = {aliases.get(name, name) for name in lock['plugins']}
    entries = marketplace['plugins']
    if len(entries) != len(expected_names) or {p['name'] for p in entries} != expected_names:
        errors.append('Marketplace selection differs from plugins.lock.json')
    sources = {f'./plugins/{name}' for name in lock['plugins']}
    if {entry['source'] for entry in entries} != sources:
        errors.append('Marketplace sources differ from bundled plugin directories')
    for entry in entries:
        source = entry['source']
        if source not in sources:
            continue
        manifest_path = root / source / '.claude-plugin/plugin.json'
        if not manifest_path.is_file():
            errors.append(f'Missing manifest: {source}')
            continue
        manifest = json.loads(manifest_path.read_text(encoding='utf-8'))
        if manifest['name'] != entry['name']:
            errors.append(f'Manifest name differs from marketplace: {source}')
        if not (root / source / 'LICENSE').is_file():
            errors.append(f'Missing upstream license: {source}')
    return errors


if __name__ == '__main__':
    project = Path(__file__).resolve().parents[1]
    try:
        failures = verify(project)
    except (OSError, ValueError, KeyError, TypeError) as error:
        print(f'Invalid plugin bundle: {error}', file=sys.stderr)
        sys.exit(1)
    if failures:
        print('\n'.join(failures), file=sys.stderr)
        sys.exit(1)
    print('Verified 14 plugins, 246 files, marketplace paths, names, and licenses.')
