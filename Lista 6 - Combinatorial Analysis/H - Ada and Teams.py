mod = 1000000007
size = 1000001

fact = [1] * size
aux = [1] * size

def getMod(x):
  return ((x % mod) + mod) % mod

def getModAux(a):
  return pow(a, mod - 2, mod)

def find(a , b):
  if (b > a):
    return 0
  return getMod(getMod(fact[a] * aux[b]) * aux[a - b])

for i in range(1,size):
    fact[i] = getMod(fact[i-1] * i)
    aux[i] = getModAux(fact[i])

while True:
  try:
    n,a,b,d = map(int,raw_input().split())
    c1,c2 = find(n, a), find(b, d)
    
    print getMod(c1 * pow(c2, a, mod)) 
  except EOFError:
    break
