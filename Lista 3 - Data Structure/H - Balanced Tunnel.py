n = int(raw_input())

ids_in = map(int, raw_input().split())
ids_out = map(int, raw_input().split())

index = [0] * (n+1)
aux = [0] * (n+1)

for i in range(n):
  index[ids_out[i]] = i

for i in range(n):
  aux[i] = index[ids_in[i]]

max = -1
answer = 0

for i in range(n):
  if (aux[i] > max):
    max = aux[i]
  else:
    answer+= 1

print answer
