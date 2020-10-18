n = int(raw_input())

sequencia = []
aux = [0] * 1000001
ascent = [0] * n

answer = 0
cont = 0

for i in range(n):

  l = list(map(int, raw_input().split()))
  sequencia.append(l[1:])

  for j in range(1, l[0]):
    if l[j] < l[j+1]:
      ascent[i] = 1
      cont += 1
      answer += n
      break
  if not ascent[i]:
    aux[l[1]] += 1

for i in range(1, len(aux)):
  aux[i] += aux[i-1]

for i in range(n):
  if not ascent[i]:
    answer += cont
    answer += aux[-1] - aux[sequencia[i][-1]]

print answer
