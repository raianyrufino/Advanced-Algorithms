n = int(raw_input())
employees = map(int, raw_input().split())
m = int(raw_input())

aux = n * [-1]  

for i in range(m):
  a, b, c= map(int, raw_input().split())
  b -= 1

  if aux[b] == -1:
    aux[b] = c
  else:
    aux[b] = min(aux[b], c) 
 
if aux.count(-1) > 1:
  print -1
else:
  print sum(aux) + 1
