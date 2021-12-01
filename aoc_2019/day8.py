def to_layers(img, n):
  return [img[i:i + n] for i in range(0, len(img), n)]

def phase1(layers):
  min_zeroes = float('inf')
  min_layer = []
  for layer in layers:
    zeroes = layer.count('0')
    if zeroes < min_zeroes:
      min_zeroes = zeroes
      min_layer = layer
  return min_layer.count('1') * min_layer.count('2')

def phase2(layers, x, y):
  image = [2] * x * y
  for layer in layers:
    for i in range(x*y):
      if image[i] == 2 and layer[i] != '2':
        image[i] = layer[i]
  return to_layers(image, x) 
  
if __name__ == "__main__":
  with open('./input/day8') as f:
    layers = to_layers(next(f), 25 * 6)
    print(phase1(layers))
    for line in phase2(layers, 25, 6):
      print(''.join(map(str, line)).replace('1','.').replace('0',' '))