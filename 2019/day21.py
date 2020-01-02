from intcode_computer import intcode_computer

if __name__ == "__main__":
  with open('./input/day21') as f:
    code = [int(i) for i in next(f).split(',')]
    print(intcode_computer(code)
      .input_ASCII('NOT C J')
      .input_ASCII('AND D J')
      .input_ASCII('NOT A T')
      .input_ASCII('OR T J')
      .input_ASCII('WALK')
      .execute().output())    
    print(intcode_computer(code)
      .input_ASCII('NOT C J')
      .input_ASCII('AND D J')
      .input_ASCII('AND H J')
      .input_ASCII('NOT B T')
      .input_ASCII('AND D T')
      .input_ASCII('OR T J')
      .input_ASCII('NOT A T')
      .input_ASCII('OR T J')
      .input_ASCII('RUN')
      .execute().output())