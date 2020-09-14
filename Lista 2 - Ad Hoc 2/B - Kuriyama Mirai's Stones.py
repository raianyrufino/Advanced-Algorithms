n = int(raw_input())
stones = map(int, raw_input().split())

m = int(raw_input())

stones_order = list(stones)
stones_order.sort()

stones_sum = [0]
stones_sum_order = [0]

for i in range(1, len(stones)+1):
  stones_sum.append(stones_sum[i-1] + stones[i-1])

for i in range(1, len(stones_order)+1):
  stones_sum_order.append(stones_sum_order[i-1] + stones_order[i-1])

for i in range(m):

  question, l, r = map(int, raw_input().split())
  answer = 0

  if question == 1:
    answer = stones_sum[r]-stones_sum[l-1]
  else:
    answer = stones_sum_order[r]-stones_sum_order[l-1]
  
  print answer
