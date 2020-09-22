n = int(raw_input())

registers = dict()

for i in range(n):
  string = raw_input()
  if registers.get(string) == None:
    registers[string] = 0
    print 'OK'
  else:
    registers[string] += 1
    print string + str(registers.get(string))
