def is_password_valid(pwd):
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
  return (2 in seen)

if __name__ == "__main__":
  sum = 0
  for i in range(183564,657474):
    if is_password_valid(i):
      sum += 1
  print(sum)