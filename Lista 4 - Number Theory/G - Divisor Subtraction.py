n = int(raw_input())

def prime(n):
  j = 2
  while j*j <= n: 
    if n % j == 0:
      return j
    j+=1
  return n
  

cont = 0

if n%2 != 0:
  n -= prime(n)
  cont += 1

print cont+(n/2)
