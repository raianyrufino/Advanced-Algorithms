def is_prime(n):
  for i in range(2, n):
    if (n % i == 0):
      return False
  return True

def find_number(n, cont):
  if not is_prime(n*cont+1):
    return cont
  return find_number(n, cont+1)

x = int(raw_input())

print find_number(x, 1)
