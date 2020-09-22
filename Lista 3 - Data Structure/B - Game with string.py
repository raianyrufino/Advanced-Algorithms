string = raw_input()

s = list(string)
player = True
cont = 0

for i in range(len(s)-1):
  if cont >= len(s)-1:
    break
  if(s[cont] == s[cont+1]):
    s.pop(cont)
    s.pop(cont)
    if(cont != 0):
      cont -=1
    
    player = not player
  else:
    cont += 1
    
if(player):
  print("No")
else:
  print("Yes")
