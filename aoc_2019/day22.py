import re

def shuffle(instructions, deck_length, deck_init=None):
  if deck_init is None:
    deck = [i for i in range(deck_length)]
  else: deck = deck_init
  for instruction in instructions:
    matches = re.match(U'([^\\d-]+)(-?\\d*)',instruction)
    if matches.group(1) == 'deal into new stack':
      deck.reverse()
    elif matches.group(1) == 'cut ':
      arg = int(matches.group(2))
      deck = deck[arg:] + deck[:arg]
    elif matches.group(1) == 'deal with increment ':
      arg = int(matches.group(2))
      t = [0] * deck_length
      for i in range(deck_length): t[(i*arg)%deck_length] = deck[i]
      deck = t
    else: print("no match")
  return deck

def track_card(instructions, deck_length, card):
  position = card
  for instruction in instructions:
    matches = re.match(U'([^\\d-]+)(-?\\d*)',instruction)
    if matches.group(1) == 'deal into new stack':
      position = deck_length - position - 1
    elif matches.group(1) == 'cut ':
      arg = int(matches.group(2))
      if arg < 0: arg = deck_length + arg
      if arg <= position: position -= arg
      else: position += deck_length - arg
    elif matches.group(1) == 'deal with increment ':
      arg = int(matches.group(2))
      position = (arg * position) % deck_length
    else: print("no match")
  return position


if __name__ == "__main__":
  with open('./input/day22') as f:
    instructions = [line.rstrip('\n') for line in f]
    print(shuffle(instructions,10007).index(2019))

    deck = None
    for i in range(101741582076661):
      if i%10000 == 0: print(i)
      deck = shuffle(instructions,119315717514047,deck)
    print(deck[2020])