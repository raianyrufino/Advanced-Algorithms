n = int(raw_input())

def dfs(x):
  if x in visited:
    return
  else:
    visited.append(x)
    for i in range(len(graph)):
      if (graph[i] != x) and ((graph[i][0] == x[0]) or (graph[i][1] == x[1])):
        dfs(graph[i])

graph = []
visited = []
cont = 0
 
for i in range(n):
	coordinates = list(map(int,raw_input().split()))
	graph.append(coordinates)

for i in range(len(graph)):
	if graph[i] not in visited :
		dfs(graph[i])
		cont += 1
 
print cont-1
