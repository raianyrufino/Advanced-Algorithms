mod = 1000000007

string = raw_input()

lista_string = list(string)

answer = 0
cont = 0

while lista_string:
  if 'a'== lista_string.pop():
    answer += cont
    cont = (cont * 2) % mod
  else:
    cont += 1
    
print answer % mods
