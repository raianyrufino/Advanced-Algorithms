def lmc(n):
  if n%2 == 0:
    return "%d %d" %(n/2, n/2)
  
  answer = -1
  j = 2
  while (j*j) <= n:
    if n%j == 0:
      answer = max(answer, j)
      answer = max(answer, n/j)
    j += 1
  
  if answer == -1:
    answer = 1

  return "%d %d" %(answer, n-answer)

t = int(raw_input())

for i in range(t):
  n = int(raw_input())
  
  print lmc(n)
