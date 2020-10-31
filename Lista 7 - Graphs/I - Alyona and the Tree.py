n = int(raw_input())
a = [[]  for i in range(n+2)]
p = map(int, raw_input().split())

p.insert(0, 0)

for i in range(n-1):
	x, y = map(int, raw_input().split())
	a[x].append((i+2,y))
 
cont = 0
aux = [(1,0)]
 
while aux:
	node, dist = aux.pop()

	if dist > p[node]:
		continue

	cont += 1
  
	for x,y in a[node]:
		aux.append((x,max(0,dist+y)))
 
print n-cont

