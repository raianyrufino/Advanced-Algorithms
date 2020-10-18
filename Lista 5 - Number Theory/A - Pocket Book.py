n, m = map(int,raw_input().split())

words=[]
answer = 1
mod = 1000000007 

for i in range(n):
	word = raw_input()
	words.append(word)

for i in range(m):
	aux=[]
	for j in range(n):
		aux.append(words[j][i])

	answer *= len(set(aux))
	answer %= mod

print answer
