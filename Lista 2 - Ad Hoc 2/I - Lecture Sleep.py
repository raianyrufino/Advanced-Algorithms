n, k = map(int, raw_input().split())

teoremas = map(int, raw_input().split())
comportamentos = map(int, raw_input().split())

aux = [0]
answer = 0
maximo = 0

for i in range(len(comportamentos)):
  if comportamentos[i]:
    answer += teoremas[i]
    teoremas[i] = 0 

for i in range(1, len(comportamentos)+1):
  aux.append(teoremas[i-1] + aux[i-1])

for i in range(n, k-1, -1):
  if maximo < (aux[i] - aux[i-k]):
    maximo = aux[i] - aux[i-k]

print maximo + answer
