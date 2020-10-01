n, m = map(int,raw_input().split())

a = map(int,raw_input().split())
b = map(int,raw_input().split())

b.sort()

aux = []

for i in range(n):
  aux.append((b[0]-a[i]) % m)

aux = list(set(aux))

for i in aux:
  q = []
  for j in range(n):
    q.append((a[j]+i) % m)
  q.sort()
  if q == b:
    print i
    break
