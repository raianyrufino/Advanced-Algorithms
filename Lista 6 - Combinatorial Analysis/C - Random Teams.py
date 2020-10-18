def max(n, m):
  return ((n - m) * (n - m + 1)) / 2
 
def min(n, m):
  aux = n / m
  rest = n % m
  return m * aux * (aux - 1) / 2 + aux * rest
 
n, m = map(int, raw_input().split())
 
print min(n, m), max(n, m)

