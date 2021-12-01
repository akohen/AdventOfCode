from pathlib import Path
import ast
import sys

TEST_MODE = bool(len(sys.argv) > 1 and sys.argv[1] == "test")

class Visitor(ast.NodeTransformer):
    def visit_Sub(self, node):
        return ast.Mult()
    def visit_Div(self, node):
        return ast.Add()

def phase1(data):
    total = 0
    for line in data:
        node = Visitor().visit(ast.parse(line.replace("*","-"), mode='eval'))
        total += eval(compile(node, filename="<ast>", mode="eval"))
    return total

def phase2(data):
    total = 0
    for line in data:
        node = Visitor().visit(ast.parse(line.replace("*","-").replace("+","/"), mode='eval'))
        total += eval(compile(node, filename="<ast>", mode="eval"))
    return total


if __name__ == "__main__":
    with Path(__file__).parent.joinpath("input/day18_sample" if TEST_MODE else "input/day18").open() as f:
        DATA = [line.strip() for line in f]

        print(f'Phase 1: {phase1(DATA)}')
        print(f'Phase 2: {phase2(DATA)}')