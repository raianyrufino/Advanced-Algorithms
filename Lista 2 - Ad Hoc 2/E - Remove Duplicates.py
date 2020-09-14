n = int(raw_input())

numbers = map(int, raw_input().split())

aux = [0] * 1001
answer = []

for i in range(n-1, -1, -1):
  if not (aux[numbers[i]]):
    answer.append(numbers[i])
    aux[numbers[i]] = 1

print len(answer)

for i in reversed(answer):
  print i,
