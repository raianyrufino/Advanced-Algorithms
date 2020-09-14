n = int(raw_input())

for i in range(n):

  string = raw_input()
  cont_alice = 0
  cont_bob = 0

  aux = string.split('0')

  for i in range(len(aux)):
    if (i%2 == 0):
      cont_alice += len(max(aux))
      aux.remove(max(aux))
    else:
      cont_bob += len(max(aux))
      aux.remove(max(aux))
  
  print cont_alice

