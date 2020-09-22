n = int(raw_input())

words = {}

for i in range(n):
  old_key, new_key = map(str, raw_input().split())
  
  if words.get(old_key) == None:
    words[new_key] = old_key
  else:
    aux = words.get(old_key)
    words.pop(old_key)
    words[new_key] = aux

print len(words)
for string in words:
  print words.get(string), string
