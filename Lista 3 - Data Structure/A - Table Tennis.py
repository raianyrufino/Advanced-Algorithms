n, k = map(int, raw_input().split())

powers = map(int, raw_input().split())

cont = 0
player = powers[0]

for i in range(1,len(powers)):
  if cont == k:
    break
  if player > powers[i]:
    cont += 1
  else:
    player = powers[i]
    cont = 1

print player
