n, m = map(int, raw_input().split())
problems = map(int, raw_input().split())

aux = [0] * 10000007
total = [0] * 10000007

answer = ''
index = 1

for i in range(m):
  aux[problems[i]] += 1
  total[aux[problems[i]]] += 1

  if total[index] == n:
    answer += '1'
    index += 1
  else:
    answer += '0'

print answer
