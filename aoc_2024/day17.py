from pathlib import Path

class chronospatial_computer:
    def __init__(self, registers=[0,0,0], program=[]):
        self.pointer = 0
        self.program = program.copy()
        self.opcodes = {
            0: self._adv,
            1: self._bxl,
            2: self._bst,
            3: self._jnz,
            4: self._bxc,
            5: self._out,
            6: self._bdv,
            7: self._cdv
        }
        self.registers = registers.copy()
        self.output = []

    def _combo_operand(self, operand):
        if operand < 4: 
            return operand
        return self.registers[operand - 4]

    def _adv(self, operand):
        self.registers[0] = self.registers[0] // 2 ** self._combo_operand(operand)

    def _bxl(self, operand):
        self.registers[1] = self.registers[1] ^ operand

    def _bst(self, operand):
        self.registers[1] = self._combo_operand(operand) % 8

    def _jnz(self, operand):
        if self.registers[0] != 0:
            self.pointer = operand - 2

    def _bxc(self, _):
        self.registers[1] = self.registers[1] ^ self.registers[2]

    def _out(self, operand):
        self.output.append(self._combo_operand(operand) % 8)

    def _bdv(self, operand):
        self.registers[1] = self.registers[0] // 2 ** self._combo_operand(operand)

    def _cdv(self, operand):
        self.registers[2] = self.registers[0] // 2 ** self._combo_operand(operand)

    def run(self):
        while self.pointer < len(self.program):
            opcode = self.program[self.pointer]
            operand = self.program[self.pointer + 1]
            self.opcodes[opcode](operand)
            self.pointer += 2
    
    def run_and_output(self):
        self.run()
        return ",".join(map(str,self.output))

def part1(registers, program):
    computer = chronospatial_computer(registers, program)
    return computer.run_and_output()


def part2(_, program):
    a = 0
    for _ in range(len(program)):
        a *= 8
        for _ in range(64):
            comp = chronospatial_computer([a, 0, 0], program)
            comp.run()
            if comp.output == program[-len(comp.output):]:
                break
            a += 1

    return a


def parse(file):
    raw_registers, raw_program = file.split("\n\n")
    registers = [int(line.split(": ")[1]) for line in raw_registers.split("\n")]
    program = [int(x) for x in raw_program.split("Program: ")[1].split(",")]
    return registers, program


if __name__ == "__main__":
    with Path(__file__).parent.joinpath("input/"+Path(__file__).stem).open(encoding="UTF-8") as f:
        DATA = parse(f.read())

        print(f"Phase 1: {part1(*DATA)}")
        print(f"Phase 2: {part2(*DATA)}")
