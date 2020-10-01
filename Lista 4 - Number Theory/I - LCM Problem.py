def lmc(l, r):
  if (2*l > r):
    return "-1 -1"
  return "%d %d" %(l, 2*l)

n = int(raw_input())

for i in range(n):
  l, r = map(int, raw_input().split())

  print lmc(l,r)
