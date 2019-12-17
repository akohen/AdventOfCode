from intcode_computer import intcode_computer

def find_inter(scaffolds):
  inter = []
  for j in range(1, len(scaffolds) - 2):
    for i in range(1, 48):
      if ( scaffolds[j][i] == 35 and 
      scaffolds[j-1][i] == 35 and 
      scaffolds[j+1][i] == 35 and scaffolds[j][i+1] == 35 and scaffolds[j][i-1] == 35 ):
        inter.append((i,j))
  
  total = 0
  for i in inter:
    total += i[0] * i[1]
  return total

def string_2_ASCII(string):
  return [ord(c) for c in string] + [10]

if __name__ == "__main__":
  with open('./input/day17') as f:
    program = [int(i) for i in next(f).split(',')]
    comp = intcode_computer(program)
    comp.execute()
    lines = [comp.output_values[i:i + 50] for i in range(0, len(comp.output_values), 50)]
    print(find_inter(lines))
    main = string_2_ASCII("A,B,A,B,A,C,A,C,B,C")
    A = string_2_ASCII("R,6,L,10,R,10,R,10")
    B = string_2_ASCII("L,10,L,12,R,10")
    C = string_2_ASCII("R,6,L,12,L,10")
    video = string_2_ASCII("n")
    
    program[0] = 2
    comp = intcode_computer(program, main + A + B + C + video)
    comp.execute()
    res = comp.output_values.pop()
    print("".join(map(chr,comp.output_values)))
    print(res)