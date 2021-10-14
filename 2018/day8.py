from pathlib import Path
import sys

TEST_MODE = bool(len(sys.argv) > 1 and sys.argv[1] == "test")

def create_node(parent, headers):
    new_node = {"children": [], "data": [], "parent": parent, "headers": headers}
    if parent: parent["children"].append(new_node)
    return new_node

def sum_metadata(node):
    total = sum(node["data"])
    for child in node["children"]:
        total += sum_metadata(child)
    return total

def get_node_value(node):
    if node["headers"][0] == 0:
        return sum(node["data"])
    total = 0
    for i in node["data"]:
        if i <= len(node["children"]):
            total += get_node_value(node["children"][i-1])
    return total

def process_input(value, current):
    if len(current["headers"]) < 2:
        current["headers"].append(value)
    elif len(current["children"]) < current["headers"][0]:
        current = create_node(current, [value])
    elif len(current["data"]) < current["headers"][1]:
        current["data"].append(value)
    else:
        current = process_input(value, current["parent"])
    return current

if __name__ == "__main__":
    with Path(__file__).parent.joinpath("input/day8_sample" if TEST_MODE else "input/day8").open() as f:

        current = create_node(None, [])
        for i in [int(i) for i in f.read().split(' ')]:
            current = process_input(i, current)

        print('Phase 1: {}'.format(sum_metadata(current)))
        print('Phase 2: {}'.format(get_node_value(current)))