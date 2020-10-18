n = int(raw_input())

dicionary = {}
answer = 0

for i in range(n):
  name = raw_input()
  dicionary[name[0]] = dicionary.get(name[0],0) + 1
    
for i in dicionary:
  answer += ((dicionary[i] / 2) * ((dicionary[i] / 2) -1 )) / 2
  answer += ((dicionary[i] - (dicionary[i] / 2)) * ((dicionary[i] - (dicionary[i] / 2)) - 1)) / 2

print answer
