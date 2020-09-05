entradas = map(int, raw_input().split())
robos = map(int, raw_input().split())

k = entradas[1]
index = 0
robos.insert(0, -1)

for i in range(len(robos)):
  if(i*(i+1)/2 == k):
    index = i
    break
  if(i*(i+1)/2 > k):
    index = k-(i*(i-1)/2)
    break
    
print robos[index]

