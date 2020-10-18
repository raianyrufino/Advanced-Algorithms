string = raw_input()

mod = 1000000007
cont = 1
aux = []

string += 'b'
 
for i in range(len(string)):
  if string[i] == 'a':
    cont += 1
  if (string[i] == 'b') and (cont > 0):
    aux.append(cont)
    cont = 1
 
answer = 1
 
for i in aux:
  answer *= i
  answer %= mod
 
print (answer - 1) % mod
