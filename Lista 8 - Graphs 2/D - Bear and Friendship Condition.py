n, m = [int(x) for x in raw_input().split()]

dic = {}
visited = set()

answer = 'YES'

for i in range(m):
  a, b = map(int, raw_input().split())
  dic.setdefault(a, {a}).add(b)
  dic.setdefault(b, {b}).add(a)

for i, j in dic.items():
  if i not in visited:
    if all([dic[aux]==j for aux in j]):
      visited.update(j)
    else:
      answer = 'NO'
      break

print answer
