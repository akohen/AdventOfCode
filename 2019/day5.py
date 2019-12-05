import operator

class intcode_computer:
  
  def __init__(self, program, input_values=[]):
    self.pointer = 0
    self.program = list(program)
    self.opcodes = {
      1: self.addition, 2: self.multiplication, 
      3: self.input, 4: self.output, 
      5: self.jump(operator.ne), 6: self.jump(operator.eq),
      7: self.comp(operator.lt), 8: self.comp(operator.eq),
      99: lambda _: True}
    self.input_values = input_values
    self.output_values = []

  def __repr__(self):
    return '\n'.join([str(e) for e in self.output_values])
  
  def read(self, mode='1'):
    value = self.program[self.pointer]
    self.pointer += 1
    if(mode == '0'): return self.program[value]
    elif(mode == '1'): return value
    else: raise Exception('Unknown parameter mode')

  def write(self, value):
    self.program[self.read()] = value
  
  def parse_instruction(self, instr): # returns (opcode, modes)
    return (instr % 100, str(instr // 100).zfill(3)[::-1])

  def addition(self, modes):
    self.write(self.read(modes[0]) + self.read(modes[1]))

  def multiplication(self, modes):
    self.write(self.read(modes[0]) * self.read(modes[1]))

  def input(self, modes):
    self.write(self.input_values.pop())

  def output(self, modes):
    self.output_values.append(self.read(modes[0]))

  def jump(self, op): # jumps to arg1 if op(arg0,0) is true
    def _jump(modes):
      if op(self.read(modes[0]), 0):
        self.pointer = self.read(modes[1])
      else: self.pointer += 1
    return _jump
    
  def comp(self, op): # writes 1/0 if op(arg0, arg1) is true/false
    def _comp(modes):
      if op(self.read(modes[0]), self.read(modes[1])):
        self.write(1)
      else:
        self.write(0)
    return _comp

  def execute(self, debug=False):
    while self.step(debug) is not True: pass
    return self

  def step(self, debug=False):
    (opcode, modes) = self.parse_instruction(self.read())
    if debug: print(self.pointer, opcode, self.program)
    return self.opcodes[opcode](modes)

if __name__ == "__main__":
  with open('./input/day5') as f:
    program = [int(i) for i in next(f).split(',')]
    print('Step 1 : {}'.format(intcode_computer(program,[1]).execute().output_values[-1]))
    print('Step 2 : {}'.format(intcode_computer(program,[5]).execute()))
