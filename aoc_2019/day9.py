from intcode_computer import intcode_computer

if __name__ == "__main__":
  with open('./input/day9') as f:
    program = [int(i) for i in next(f).split(',')]
    print('Step 1 : {}'.format(intcode_computer(program,[1]).execute()))
    print('Step 2 : {}'.format(intcode_computer(program,[2]).execute()))