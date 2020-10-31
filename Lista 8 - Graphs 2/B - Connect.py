def isValid(x, y):
  return (0 <= x < n) and (0 <= y < n)
 
def bfs(visited, u, v):
  queue = [(u, v)]
  visited.add((u, v))

  while queue:
    u, v = queue[0]
    queue = queue[1:]

    for i in validate:
      x, y = u + i[0], v + i[1]
      if ((x, y) not in visited) and (isValid(x, y) and aux[x][y] == '0'):
        visited.add((x, y))
        queue.append((x, y))
  
n = int(raw_input())

r1, c1 = map(int, raw_input().split())
r2, c2 = map(int, raw_input().split())

r1, c1, r2, c2 = r1-1, c1-1, r2-1, c2-1

aux, start, end = [], set(), set()

validate = [[1, 0], [-1, 0], [0, 1], [0, -1]]

for i in range(n):
  string = raw_input()
  aux.append(string)

bfs(start, r1, c1)
bfs(end, r2, c2)

if (r2, c2) in start:
  print 0
else:
  answer = int(1e9)
  for i in start:
    for j in end:
      answer = min(answer, (i[0] - j[0]) * 2 + (i[1] - j[1]) * 2)
  print answers
