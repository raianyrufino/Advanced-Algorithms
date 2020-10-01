import math

n = int(raw_input())

aux = [0] * 2000006

m = 1

for i in range(2, n+1):
  flag = 0
  for j in range(2, int(round(math.sqrt(i), 0))+1):
    if (i % j == 0):
      flag = 1
      break

  if flag == 0:
    aux[i] = m
    m += 1
  else:
    aux[i] = aux[j]

for i in range(2, n+1):
  print aux[i],
