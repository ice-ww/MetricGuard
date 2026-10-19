"""Validate local links in tracked acceptance Markdown against the Git index."""
from pathlib import Path
import gzip
import json
import subprocess
from urllib.parse import unquote, urlsplit
import xml.etree.ElementTree as ET
import zlib

from markdown_it import MarkdownIt


def check(root: Path) -> int:
    result = subprocess.run(['git', '-C', str(root), 'ls-files', '-z'],
                            check=True, capture_output=True)
    tracked = {name for name in result.stdout.decode('utf-8').split('\0') if name}
    reports = sorted(name for name in tracked
                     if name.startswith('docs/validation/') and name.endswith('.md'))
    if not reports:
        print('evidence: no tracked acceptance reports in docs/validation')
        return 1
    errors = []
    parser = MarkdownIt('commonmark')
    for name in reports:
        report = root / name
        if not report.is_file():
            errors.append(f'{name}: missing report')
            continue
        for block in parser.parse(report.read_text(encoding='utf-8')):
            for token in block.children or []:
                href = token.attrGet('href') if token.type == 'link_open' else (
                    token.attrGet('src') if token.type == 'image' else None)
                if not isinstance(href, str) or not href:
                    continue
                url = urlsplit(href)
                if url.scheme or url.netloc or not url.path:
                    continue
                target = (root / unquote(url.path).lstrip('/') if url.path.startswith('/')
                          else report.parent / unquote(url.path)).resolve()
                location = f'{name}:{(block.map or [0])[0] + 1}: {href}'
                try:
                    relative = target.relative_to(root).as_posix()
                except ValueError:
                    errors.append(f'{location}: outside repository')
                    continue
                if not target.is_file():
                    errors.append(f'{location}: missing file')
                elif relative not in tracked:
                    errors.append(f'{location}: untracked file (git add required)')
                elif target.suffix == '.gz':
                    try:
                        with gzip.open(target, 'rb') as stream:
                            data = stream.read()
                        if target.name.endswith('.json.gz'):
                            json.loads(data)
                        elif target.name.endswith('.xml.gz'):
                            ET.fromstring(data)
                    except (OSError, EOFError, ValueError, UnicodeError, ET.ParseError, zlib.error) as exc:
                        errors.append(f'{location}: unreadable compressed record ({type(exc).__name__})')
    for error in errors:
        print(error)
    print(f'evidence: {len(reports)} reports, {len(errors)} errors')
    return int(bool(errors))
