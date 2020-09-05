n = int(raw_input())

for i in range(n):
  a = raw_input()
  b = raw_input()

  p = list(a)
  h = list(b)

  if (len(p) > len(h)):
    print 'NO'
  else:
    p.sort()
    flag = False
    j = 0
    
    while (j <= (len(h)-len(p))):
      temp = []

      for i in range(j, j+len(p)):
        temp  += h[i]
      
      temp.sort()
      if(p == temp):
        flag = True
        break
      j+=1

    if flag:
      print 'YES'
    else:
      print 'NO'
