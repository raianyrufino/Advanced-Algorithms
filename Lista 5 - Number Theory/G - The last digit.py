t = int(raw_input())

for i in range(t):
  a, b = map(int, raw_input().split())

  if b == 0:
    print 1
  else:
    a %= 10
    b %= 4

    if b == 0:
      b = 4
        
    print (a**b) % 10
