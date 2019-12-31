from intcode_computer import intcode_computer

if __name__ == "__main__":
  with open('./input/day25') as f:
    intcode_computer([int(i) for i in next(f).split(',')]).interactive()