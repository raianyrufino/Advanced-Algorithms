n, k = map(int,raw_input().split())

ids = map(str, raw_input().split())

aux = dict()
answer = []
 
for i in ids:
  aux[i] = 0
 
for i in ids:
  if aux[i] == 0:
    aux[i] = 1
    answer.append(i)
    if len(answer) > k:
      aux[answer.pop(0)] = 0
    
print len(answer)
print " ".join(reversed(answer))
