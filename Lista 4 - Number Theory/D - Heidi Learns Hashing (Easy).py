def find_pair(r):
  if (r < 5) or (r % 2 == 0):
    return 'NO'
  else:
    return "1 %d" %((r-3)/2)

r = int(raw_input())

print find_pair(r)
