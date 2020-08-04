import os
import sys
import pathlib
import re
import xml.etree.ElementTree as Xml


def parse_id(coord: str) -> (str, str):
    m = rx_coord.match(coord)
    if m is None:
        print(
            'Invalid format: %s; must be {x,y} (braces can be omitted).' % coord
        )
        return None
    return m.group(1, 2)


def find_text(coord):
    (pid, tid) = parse_id(coord)
    t = root.find(f'./page[@id="{pid}"]/t[@id="{tid}"]')
    if t is None:
        return None
    print('{%s,%s} => %s' % (pid, tid, t.text))
    return t.text


if len(sys.argv) < 2:
    print(f'{os.path.basename(__file__)} <path> [language-code]')
    print("""
    Language codes:
    88 - Chinese, Traditional
    86 - Chinese, Simplified
    82 - Korean
    81 - Japanese
    55 - Portuguese
    49 - German
    48 - Polish
    44 - English
    42 - Czech
    39 - Italian
    34 - Spanish
    33 - French
    07 - Russian

    """)
    exit(1)

# Path to root of unpacked resource files
# X4SRC = '../../unpacked'
# X4SRC = 'E:/Games/X-Universe/X4/modding/unpacked/t/0001-L044.xml'

LANG = 44
X4SRC = sys.argv[1]
if len(sys.argv) >= 3:
    LANG = sys.argv[2]

rx_coord = re.compile(r'{?\s*(\d+)\s*,\s*(\d+)\s*\}?')
rx_id = re.compile(r'({\s*\d+\s*,\s*\d+\s*\})')

filepath = pathlib.Path(__file__).parent.absolute()
lang_file = f't/0001-L0{LANG}.xml'
filepath = filepath.joinpath(X4SRC, lang_file)
filepath = filepath.resolve()
if not filepath.exists():
    print('file not found: ', filepath)
    exit(1)

print('loading file...')
tree = Xml.parse(filepath)
root = tree.getroot()
print('ready.')

while True:
    cmd = input('{} ')
    if 'exit' == cmd.lower():
        break

    sids = [cmd]
    while sids:
        nr = []
        for sid in sids:
            if not sid:
                continue
            text = find_text(sid)
            if text is None:
                print('%s not found' % sid)
                continue
            matches = rx_id.findall(text)
            if matches:
                nr += matches
        sids = nr
        if not sids:
            print()
