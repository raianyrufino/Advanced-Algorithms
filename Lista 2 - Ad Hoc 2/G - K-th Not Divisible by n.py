def not_divisible_by_n(n,k):
  x = k/(n-1)
  answer = k-x*(n-1)

  if(k == x*(n-1)):
    answer -= 1
  answer += x*n

  return answer

t = int(raw_input())

for i in range(t):
  n, k = map(int, raw_input().split())

  print not_divisible_by_n(n, k)

