def dfs(node, x, color):
  visited[node] = True
 
  if node == x:
   return True
 
  for i, c in graph[node]:
    if (c == color) and not visited[i]:
      if dfs(i, x, color):
        return True
  return False
 
 
n, m = map(int, raw_input().split())
 
graph = [[] for i in range(n+1)]

for i in range(m):
  a, b, c = map(int, raw_input().split())
  graph[a].append((b, c))
  graph[b].append((a, c))
 
q = int(raw_input())

for i in range(q):
  u, v = map(int, raw_input().split())
    
  cont = 0 
  for j in range(1, 101):
    visited = [0] * (n+1)
    if (dfs(u, v, j)):
      cont += 1
 
  print cont
