n = int(raw_input())

aux = []
groups = 0

for i in range(n):
  p = int(raw_input())
  aux.append(p)

for i in range(n):
  cont = 0
  j = aux[i]

  while j != -1:
    cont += 1
    j = aux[j-1]

  groups = max(cont, groups)
  
print groups + 1
