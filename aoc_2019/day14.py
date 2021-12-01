import math

def get_reactions(puzzleInput):
  reactions = {}
  for line in puzzleInput:
    [input_chems,output_chem] = line.split(' => ')
    [qty, output_chem] = output_chem.split(' ')
    output_chem = reactions.setdefault(output_chem, {'inputs':{}, 'produced': 0, 'available': 0})
    output_chem['qty'] = int(qty)
    for input_chem in input_chems.split(', '):
      [in_qty, in_chem] = input_chem.split(' ')
      reactions.setdefault(in_chem, {'inputs':{}, 'produced': 0, 'available': 0})
      output_chem['inputs'][in_chem] = int(in_qty)
  reactions['ORE']['qty'] = 1
  return reactions

def produce(reactions, target='FUEL', qty=1):
  batches = math.ceil((qty - reactions[target]['available']) / reactions[target]['qty'])
  if batches < 1: return
  for input_chem in reactions[target]['inputs']:
    produce(reactions, input_chem, reactions[target]['inputs'][input_chem] * batches)
    reactions[input_chem]['available'] -= reactions[target]['inputs'][input_chem] * batches
  reactions[target]['available'] += reactions[target]['qty'] * batches
  reactions[target]['produced'] += reactions[target]['qty'] * batches


if __name__ == "__main__":
  with open('./input/day14') as f:
    reactions = [line.rstrip('\n') for line in f]
    res = get_reactions(reactions)
    produce(res, 'FUEL', 4906796)
    print(1000000000000 - res['ORE']['produced'])