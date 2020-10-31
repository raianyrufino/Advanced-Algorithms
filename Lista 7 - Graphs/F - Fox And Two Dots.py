import sys

sys.setrecursionlimit(10000)

def isValid(x, y):
  return (0 <= x < n) and (0 <= y < m)

def dfs(x, y, dit_x = -1, dit_y = -1):
    aux[x][y] = True
    for i in range(4):
      aux_x = x + dx[i]
      aux_y = y + dy[i]
      if isValid(aux_x, aux_y) and strings[x][y] == strings[aux_x][aux_y]:
        if aux[aux_x][aux_y] and not (aux_x == dit_x and aux_y == dit_y):
          print 'Yes'
          sys.exit(0)
        if not aux[aux_x][aux_y]:
          dfs(aux_x, aux_y, x, y)
 
n, m = map(int, raw_input().split())

strings = []

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

for i in range(n):
  strings.append(raw_input())

aux = [[False] * m for i in range(n)]

for i in range(n):
  for j in range(m):
    if not aux[i][j]:
      dfs(i, j)

print 'No'
