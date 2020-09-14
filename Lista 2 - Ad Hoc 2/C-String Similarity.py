def find_similarity(n, s):
  answer = []
  index = 0

  for i in range(n):
    aux = s[i:i+n]
    if len(aux) == n:
      answer.append(aux[index])
      index+=1
  return ''.join(answer)

t = int(raw_input())
 
for i in range(t):
  n = int(raw_input())
  s = list(raw_input())
  
  print find_similarity(n, s)
