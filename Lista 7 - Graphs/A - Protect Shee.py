r, c = map(int, raw_input().split())
 
aux = []
 
for i in xrange(r):
  string = list(raw_input().strip())
  aux.append(string)
 
status = False
 
for x in range(r):
    for y in range(c):
        if aux[x][y] == ".":
            aux[x][y] = "D"
            continue
        
        if aux[x][y] == "S":
            if (x - 1) >= 0 and aux[x-1][y] == "W":
                status = True
            if (x + 1) < r and aux[x+1][y] == "W":
                status = True
            if (y - 1) >= 0 and aux[x][y-1] == "W":
                status = True
            if (y + 1) < c and aux[x][y+1] == "W":
                status = True
 
if status:
    print "NO"
else:
    print "YES"
    for row in aux:
        print "".join(row)
