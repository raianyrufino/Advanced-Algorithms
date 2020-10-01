aux = [0] * 1002

numbers = []

def check(y, p):
  while y % p == 0:
    y /= p

  if y == 1:
    return True
  return False

n = int(raw_input())

cont = 0

for i in range(2, n+1):
  if aux[i] == 0:
    cont += 1 
    numbers.append(i)
    
    j = 2
    while j*i <= n:
      if check(j, i):
        cont += 1
        numbers.append(j*i)
      aux[j*i] = 1
      j+=1

print cont
for number in numbers:
  print number,
