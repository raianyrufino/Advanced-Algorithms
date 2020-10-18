mod = 1000000007

def find_pairs(string):
  answer = 0

  for i in string:
    if i >= '0' and i <= '9':
      aux = ord(i)-48
      answer += 6-bin(aux).count("1")
 
    if i >= 'A' and i <= 'Z':
      aux = ord(i)-55
      answer += 6-bin(aux).count("1")
 
    if i >= 'a' and i <= 'z':
      aux = ord(i)-61
      answer += 6-bin(aux).count("1")
 
    if i == '-':
      answer += 6-bin(62).count("1")
 
    if i == '_':
      answer += 6-bin(63).count("1")
 
  return (3**answer)%(mod)
    
string = raw_input()

print find_pairs(string)
