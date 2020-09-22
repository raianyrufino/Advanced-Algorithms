n = int(raw_input())

for i in range(n):
  string = raw_input()

  cont = max(string.split('R'), key=len)
  print len(cont)+1
