def no_duplicates(string):
  size = len(string)
  answer = ''
  j = 0

  if (size <= 1):
    return answer
  else:
    while(j < size):
      if (j != size-1):
        if(string[j] != string[j+1]):
          if (string[j] not in answer):
            answer += string[j]
          j+=1
        else:
          j+=2
      else:
        if(string[j] not in answer):
          answer += string[j]
        j += 1
  return answer

n = int(raw_input())

for i in range(n):

  string = raw_input()

  print(''.join(sorted(no_duplicates(string))))
    
