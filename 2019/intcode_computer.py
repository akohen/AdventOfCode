import operator

class intcode_computer:
  
  def __init__(self, program, input_values=[], stop_on_output=False):
    self.pointer = 0
    self.program = list(program)
    self.opcodes = {
      1: self._addition, 2: self._multiplication, 
      3: self._input, 4: self._output, 
      5: self._jump(operator.ne), 6: self._jump(operator.eq),
      7: self._comp(operator.lt), 8: self._comp(operator.eq),
      9: self._shift_base,
      99: self._halt}
    self.input_values = input_values
    self.output_values = []
    self.rel_base = 0
    self.stop_on_output = stop_on_output
    self.halted = False

  def __repr__(self):
    return '\n'.join([str(e) for e in self.output_values])
  
  def _read(self, mode='1'):
    if(mode == '0'): address = self.program[self.pointer]
    elif(mode == '1'): address = self.pointer
    elif(mode == '2'): address = self.program[self.pointer] + self.rel_base
    else: raise Exception('Unknown parameter mode')
    self._resize_memory(address)
    self.pointer += 1
    return self.program[address]

  def _write(self, value, mode='0'):
    if(mode == '0'): address = self._read()
    elif(mode == '2'): address = self._read() + self.rel_base
    else: raise Exception('Unknown parameter mode')
    self._resize_memory(address)
    self.program[address] = value

  def _resize_memory(self, address):
    if(address > len(self.program)-1):
      self.program += [0] * (address - len(self.program) +1)
  
  def _parse_instruction(self, instr): # returns (opcode, modes)
    return (instr % 100, str(instr // 100).zfill(3)[::-1])

  def _addition(self, modes):
    self._write(self._read(modes[0]) + self._read(modes[1]), modes[2])

  def _multiplication(self, modes):
    self._write(self._read(modes[0]) * self._read(modes[1]), modes[2])

  def _input(self, modes):
    if len(self.input_values) == 0:
      self.pointer -= 1
      return True
    self._write(self.input_values.pop(0), modes[0])

  def _output(self, modes):
    self.output_values.append(self._read(modes[0]))
    return self.stop_on_output

  def _shift_base(self, modes):
    self.rel_base += self._read(modes[0])

  def _jump(self, op): # jumps to arg1 if op(arg0,0) is true
    def __jump(modes):
      if op(self._read(modes[0]), 0):
        self.pointer = self._read(modes[1])
      else: self.pointer += 1
    return __jump
    
  def _comp(self, op): # writes 1/0 if op(arg0, arg1) is true/false
    def __comp(modes):
      if op(self._read(modes[0]), self._read(modes[1])):
        self._write(1, modes[2])
      else:
        self._write(0, modes[2])
    return __comp

  def _halt(self, modes):
    self.halted = True
    return True

  def execute(self, debug=False):
    while self.step(debug) is not True: pass
    if debug: print(self.output_values)
    return self

  def step(self, debug=False):
    (opcode, modes) = self._parse_instruction(self._read())
    if debug: print(self.pointer, opcode, modes)
    return self.opcodes[opcode](modes)

  def input(self, value):
    if isinstance(value, list): self.input_values += value
    else: self.input_values.append(value)
    return self

  def output(self):
    return self.output_values.pop()

  def clear(self):
    del self.output_values[:]
    return self

  def interactive(self):
    def string_2_ASCII(string):
      return [ord(c) for c in string] + [10]
    while self.halted == False:
      print("".join(map(chr,self.execute().output_values)))
      self.input_values = string_2_ASCII(input(">"))
      self.clear()