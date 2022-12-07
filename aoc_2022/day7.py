from pathlib import Path

def phase1(data):
    dir_sizes = []

    def get_size(node):
        if node['type'] == 'file':
            return node['size']

        size = 0
        for child in node['contents'].values():
            size_child = get_size(child)
            if child['type'] == 'dir' and size_child < 100000:
                dir_sizes.append(size_child)
            size += size_child
        return size

    get_size(data)

    return sum(dir_sizes)


def phase2(data):
    dir_sizes = []
    total_size = 70000000
    needed_size = 30000000

    def get_size(node):
        if node['type'] == 'file':
            return node['size']

        size = 0
        for child in node['contents'].values():
            size_child = get_size(child)
            if child['type'] == 'dir':
                dir_sizes.append(size_child)
            size += size_child
        return size

    available = total_size - get_size(data)
    to_delete = needed_size - available

    return min([d for d in dir_sizes if d > to_delete])


def parse(file):
    root = {'name':'/', 'contents': {}, 'type': 'dir'}
    curr, data, i = root, file.split('\n'), 1
    while i < len(data):
        args = data[i].split(' ')
        if args[0] != '$':
            if args[0] == 'dir':
                curr['contents'][args[1]] = {'name': args[1], 'parent': curr, 'contents': {}, 'type': 'dir'}
            else:
                curr['contents'][args[1]] = {'name': args[1], 'parent': curr, 'size': int(args[0]), 'type': 'file'}
        if args[0] == '$' and args[1] == 'cd':
            if args[2] == '..':
                curr = curr['parent']
            else:
                curr = curr['contents'][args[2]]
        i+=1
    return root


if __name__ == "__main__":
    with Path(__file__).parent.joinpath("input/"+Path(__file__).stem).open(encoding="UTF-8") as f:
        DATA = parse(f.read())

        print(f"Phase 1: {phase1(DATA)}")
        print(f"Phase 2: {phase2(DATA)}")
