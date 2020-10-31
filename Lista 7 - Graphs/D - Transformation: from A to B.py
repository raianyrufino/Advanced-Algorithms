a, b = map(int, raw_input().split())
 
aux = []
aux.append(b)
 
while b > a:
  if (b % 10) == 1:
    b /= 10
    aux.append(b)
  elif (b % 2 == 0):
    b /= 2
    aux.append(b)
  else:
    print 'NO'
    exit()
 
if b == a:
  print 'YES'
  print len(aux)

  for i in reversed(aux):
   print i,
else:
  print 'NO'
