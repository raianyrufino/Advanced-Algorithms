n = int(raw_input())

aux = [''] * 26

answer = 0

for i in range(n):
  string = raw_input()
  index = ord(string[0]) - 97
  
  aux[index] += string
  aux[index] = ''.join(set(aux[index]))

for i in range(len(aux)):
  for j in range(len(aux)):
    if i != j:
      for z in aux[i]:
        if z in aux[j]:
          aux[i] += aux[j]
          aux[j] = ''

for i in aux:
  if i != '':
    answer += 1
    
print answer    
