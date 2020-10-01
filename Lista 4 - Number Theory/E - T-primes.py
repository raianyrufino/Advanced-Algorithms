size = 1000001
aux = [0] * size
aux[1] = 1

set_aux = set()

for i in range(1, size):
	if aux[i] == 0:
		set_aux.add(i*i)
		for j in range(i*i, size, i):
			aux[j] = 1

n = int(raw_input())
numbers = map(int, raw_input().split())

for number in numbers:
  if number in set_aux:
    print 'YES'
  else:
    print 'NO'
