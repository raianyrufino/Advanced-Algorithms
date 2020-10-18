import sys

flush = sys.stdout.flush
 
n = int(raw_input())
 
print('? 1 2')
flush()
 
value1 = int(raw_input())
 
print('? 2 3')
flush()
 
value2 = int(raw_input())
 
print('? 1 3')
flush()
 
value3 = int(raw_input())
 
aux3 = (value3 - value1 + value2) / 2
aux2 = value2 - aux3
aux1 = value1 - aux2
 
answer = [aux1, aux2, aux3]
 
for i in range(4, n+1):
  print('? 1 %d' % i)
  flush()

  x = int(raw_input())

  answer.append(x - aux1)
 
print '! ' + ' '.join(map(str, answer))
