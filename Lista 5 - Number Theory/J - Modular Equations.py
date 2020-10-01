a, b = map(int, raw_input().split())

if a == b:
  print 'infinity'
elif a < b:
  print 0
else:
  a -= b
  i = 1
  answer = 0

  while (i*i) <= a:
    if (a % i) == 0:
      if i > b:
        answer += 1
      if (a/i) > b and (i*i) != a:
        answer += 1
    i += 1
  print answer
