import math

def getFactorial(i, j):
  if (i + j) == t:
    aux =  math.factorial(n)/(math.factorial(n - j) * math.factorial(j))
    aux *= math.factorial(m)/(math.factorial(m - i) * math.factorial(i))
    
    return aux

n, m, t = map(int, raw_input().split())

answer = 0
 
for i in range(1, m+1):
    for j in range(4, n+1):
        if (i + j) == t:
          answer += getFactorial(i, j)

print answer
