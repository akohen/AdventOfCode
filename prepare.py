import sys
from pathlib import Path

if len(sys.argv) != 3 or not str.isdigit(sys.argv[1]) or not str.isdigit(sys.argv[2]):
    print("usage: prepare.py year day")
    print("   example: prepare.py 2022 24")
    exit(-1)


path_folder = Path(__file__).parent.joinpath("aoc_"+sys.argv[1])
file_code = Path(__file__).parent.joinpath("aoc_"+sys.argv[1]+"/day"+sys.argv[2]+".py")
file_test = Path(__file__).parent.joinpath("aoc_"+sys.argv[1]+"/day"+sys.argv[2]+"_test.py")

if not path_folder.is_dir():
    print('Failed to find folder: ' + path_folder.__str__())
    exit(-1)

if file_code.is_file():
    print('File ' + file_code.__str__() + ' already exists')
    exit(-1)

if file_test.is_file():
    print('File ' + file_test.__str__() + ' already exists')
    exit(-1)

with file_code.open('w', encoding="utf-8") as f:
    f.write("""from pathlib import Path

def part1(data):
    return data


def part2(data):
    return len(data)


def parse(file):
    return [line for line in file.split('\\n')]


if __name__ == "__main__":
    with Path(__file__).parent.joinpath("input/"+Path(__file__).stem).open(encoding="UTF-8") as f:
        DATA = parse(f.read())

        print(f"Phase 1: {part1(DATA)}")
        print(f"Phase 2: {part2(DATA)}")
""")

with file_test.open('w', encoding="utf-8") as f:
    f.write("""from aoc_{year} import day{day}

test_data = day{day}.parse(\""" \""")


def test_day{day}():
    assert day{day}.part1(test_data) == 1
    #assert day{day}.part2(test_data) == 1
""".format(year=sys.argv[1], day=sys.argv[2]))
