x = int(raw_input())

for i in range(x):
  a,b,n = map(int, raw_input().split())

  soma = a + b

  cont = 0

  while (soma < n+1):
    if (a <= b):
      a += b
      soma = a + b
      cont += 1
    else:
      b += a
      soma = b + a
      cont += 1

  print cont+1
