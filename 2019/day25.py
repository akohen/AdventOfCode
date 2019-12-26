from intcode_computer import intcode_computer

def string_2_ASCII(string):
  return [ord(c) for c in string] + [10]

if __name__ == "__main__":
  with open('./input/day25') as f:
    program = [int(i) for i in next(f).split(',')]
    comp = intcode_computer(program)
    while comp.halted is False:
      print("".join(map(chr,comp.execute().output_values)))
      val = input(">")
      print(val)
      comp.input_values = string_2_ASCII(val)
      comp.clear()
    
