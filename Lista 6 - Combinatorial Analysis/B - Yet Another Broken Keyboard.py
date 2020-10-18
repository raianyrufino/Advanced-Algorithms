n, k = map(int, raw_input().split())
string = raw_input()
letters  = map(str, raw_input().split())

cont = 0
answer = 0

for i in range(len(string)):
	if string[i] not in letters:
		answer += (cont*(cont+1))/2
		cont = 0
	else:
		cont += 1

answer += (cont*(cont+1))/2

print answer
