n, s = map(int, raw_input().split())
a = list(map(int, raw_input().split()))
b = list(map(int, raw_input().split()))

j = 1
aux = [0]

if not a[0]:
  j = 0

for i in range(1, n):
  if a[i] and b[i]:
    aux.append(i)

if max(aux) >= s and b[s-1] and j:
  print 'YES'
elif a[0] and a[s-1]:
  print 'YES'
else:
  print 'NO'
