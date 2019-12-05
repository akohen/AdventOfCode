import operator

class intcode_computer:
  
  def __init__(self, program, input_values=[]):
    self.pointer = 0
    self.program = program
    self.opcodes = {
      1: self.addition, 2: self.multiplication, 
      3: self.input, 4: self.output, 
      5: self.jump(operator.ne), 6: self.jump(operator.eq),
      7: self.comp(operator.lt), 8: self.comp(operator.eq),
      99: lambda _: False}
    self.input_values = input_values
    self.output_values = []

  def __repr__(self):
    return '\n'.join([str(e) for e in self.output_values]) 

  def get(self, value, mode):
    if(mode == '0'): return self.program[value]
    elif(mode == '1'): return value
    else: raise Exception('Unknown parameter mode')
  
  def current(self):
    val = self.program[self.pointer]
    self.pointer += 1
    return val
  
  def parse_instruction(self, instr): # returns (opcode, modes)
    return (instr % 100, str(instr // 100).zfill(3)[::-1])

  def addition(self, modes):
    value = self.get(self.current(), modes[0]) + self.get(self.current(), modes[1])
    self.program[ self.current() ] = value
    return True

  def multiplication(self, modes):
    value = self.get(self.current(), modes[0]) * self.get(self.current(), modes[1])
    self.program[ self.current() ] = value
    return True

  def input(self, modes):
    self.program[ self.current() ] = self.input_values.pop()
    return True

  def output(self, modes):
    self.output_values.append(self.get(self.current(), modes[0]))
    return True

  def jump(self, op):
    def _jump(modes):
      if op(self.get(self.current(), modes[0]), 0):
        self.pointer = self.get(self.current(), modes[1])
      else: self.current()
      return True
    return _jump
    
  def comp(self, op):
    def _comp(modes):
      if op(self.get(self.current(), modes[0]), self.get(self.current(), modes[1])):
        self.program[ self.current() ] = 1
      else:
        self.program[ self.current() ] = 0
      return True
    return _comp

  def execute(self, debug=False):
    while self.step(debug): pass
    return True

  def step(self, debug=False):
    (opcode, modes) = self.parse_instruction(self.current())
    if debug: print(self.pointer, opcode, self.program)
    return self.opcodes[opcode](modes)

if __name__ == "__main__":
  with open('./input/day5') as f:
    program = [int(i) for i in next(f).split(',')]
    comp = intcode_computer(program,[5])
    if comp.execute():
      print(comp)
    