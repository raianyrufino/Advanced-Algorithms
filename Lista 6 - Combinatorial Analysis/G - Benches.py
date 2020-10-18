n = int(raw_input())

answer = 1

for i in range(5):
	answer *= (n*n)
	n -= 1

print answer/120
