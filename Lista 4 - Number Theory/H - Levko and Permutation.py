n, k = map(int, raw_input().split())

if n == k:
  print -1
else:
  aux = n-k
  print aux,
  for i in range(1, aux):
    print i,
  for j in range(aux+1, n+1):
    print j,
