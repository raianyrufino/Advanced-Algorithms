def lmc(n):
  if n<= 2:
    return n
  
  j = 1
  cont = 0
  while j*j <= n:
    if (j*j) == n:
      cont += 1
    elif n%j == 0:
      cont += 2
    j += 1

  return cont

n = int(raw_input())

print lmc(n)
