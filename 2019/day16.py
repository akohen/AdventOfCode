from itertools import cycle, islice
from math import factorial
import scipy.special

def offset_fft(n, offset_length, phases):
  """
    This uses the fact that for input U of length l, for i > l/2:
    - U_n+1[i] = sum U_n[j] % 10 with j>i
    - U_n[i] = sum[ (k_nj) * U_0[j] ] % 10 j from i to l with k being binomial coefficients
    - U_n[l] = U_0[l]
  """
  offset = int(''.join(map(str, n[:offset_length])))

  complete_input = n * 10000
  pattern = [scipy.special.comb(i+phases-1, i, exact=True) % 10 for i in range(len(complete_input)//8)]
  result = []
  for c in range(8):
    i = c + offset
    number = 0
    for j in range(len(complete_input)-i):
      number = (number + complete_input[i+j] * pattern[j]) % 10
    result.append(number)
  return int(''.join(map(str, result)))

def fft(n, phases):

  def pattern(position):
    base_pattern = [0, 1, 0, -1]
    pattern = []
    for i in base_pattern: pattern += [i] * (position + 1)
    p = cycle(pattern)
    next(p)
    return p
  
  for count in range(phases):
    n = [abs(sum(a * b for a,b in zip(n,pattern(i)))) % 10 for i,v in enumerate(n)]
  return int(''.join(map(str, n[:8])))

if __name__ == "__main__":
  with open('./input/day16') as f:
    my_number = [int(i) for i in next(f)]
    print(fft(my_number,100))
    #offset_fft([int(i) for i in '03036732577212944063491565474664'],7,100)
    print(offset_fft(my_number,7,100))