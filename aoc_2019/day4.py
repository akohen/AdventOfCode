def is_password_valid(pwd, part2=False):
  previous = 10
  seen = [0] * 10
  while(pwd > 0):
    n = pwd % 10
    pwd = pwd // 10
    if n > previous:
      return False
    else:
      previous = n
      seen[n] += 1
  if part2:
    return (2 in seen)
  else:
    return (seen.count(0) > 4)

if __name__ == "__main__":
  (sumA, sumB) = (0,0)
  for i in range(183564,657474):
    if is_password_valid(i, True):
      sumB += 1
    elif is_password_valid(i):
      sumA += 1
  print('Part one count: {}'.format(sumA+sumB))
  print('Part two count: {}'.format(sumB))