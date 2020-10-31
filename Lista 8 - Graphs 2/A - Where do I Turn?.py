x1, y1 = map(int, raw_input().split())
x2, y2 = map(int, raw_input().split())
x3, y3 = map(int, raw_input().split())

answer = ((x2-x1)*(y3-y2)) - ((y2-y1)*(x3-x2))

if answer == 0: 
  print "TOWARDS"
elif answer > 0: 
  print "LEFT"
else: 
  print "RIGHT"
