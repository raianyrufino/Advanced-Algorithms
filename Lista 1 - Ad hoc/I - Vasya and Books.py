n = int(raw_input())

books = map(int, raw_input().split())
steps = map(int, raw_input().split())

aux = [False] * (n + 1)

index = 0
answer = ''
for i in range(len(books)):
  x = steps[i]
  if(aux[x]):
    answer += '0 '
    continue
    
  cont = 0
  while True:
    cont += 1
    aux[books[index]] = True
    if(books[index] == x):
      break
    index += 1
    
  index += 1
  answer += str(cont) + ' '

print answer
