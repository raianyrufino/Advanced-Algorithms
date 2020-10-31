from collections import defaultdict
from heapq import heappush, heappop

def dijkstra(n, start, end):
  visited = [None] * (n + 1)
  aux = [(0, start,start)]
  
  while aux:
    dist, vertice,anterior = heappop(aux)
    if visited[vertice] is None:
      visited[vertice] = dist
      previous[vertice] = anterior
      if visited[end] != None:
        return visited[end]
      for vizinho, distAresta in neighbors[vertice]:
        if visited[vizinho] is None:
          heappush(aux, (dist + distAresta, vizinho, vertice))
  
  return -1

n,m = map(int, raw_input().split())
neighbors = defaultdict(set)
previous = [[] for i in range(n+1)]

for i in range(m):
  v1,v2, p = map(int, raw_input().split())
  neighbors[v1].add((v2,p)),neighbors[v2].add((v1,p))

if dijkstra(n, 1, n) != -1:
  father, prt = n, []
  previous[1] = 0
  while father != 0:
    prt.append(father)
    father = previous[father]
  print " ".join(map(str, reversed(prt)))
else:
  print '-1'
