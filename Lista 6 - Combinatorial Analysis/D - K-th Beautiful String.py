t = int(raw_input())
 
for i in range(t):
  n, k = map(int, raw_input().split())

  cont = 0
  aux = 1
 
  while k > cont:
    cont += aux
    aux += 1
 
  indexes = [k - ((aux - 1) * (aux - 2) / 2), aux]

  answer = ''
 
  for i in range(1, n + 1):
    if (n - i + 1) in indexes:
      answer += 'b'
    else:
      answer += 'a'
  
  print answer

