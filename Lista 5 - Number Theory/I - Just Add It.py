mod = 10000007

def modExponentiation(a, b):
  a %= mod
  result = 1

  while (b > 0):
    if (b % 2 == 1):
      result = (result*a) % mod
    a = (a*a) % mod
    b = b >> 1
  
  return result

while True:
  n, k = map(int, raw_input().split())

  if (n == 0) and (k == 0):
    break
  if n == 1:
    print "1"
    continue
    
  a = (2 * modExponentiation(n-1, n-1))
  b = modExponentiation(n, n)
  c = (2 * modExponentiation(n-1, k))
  d = (modExponentiation(n, k))

  print (a + b + c + d) % mod

