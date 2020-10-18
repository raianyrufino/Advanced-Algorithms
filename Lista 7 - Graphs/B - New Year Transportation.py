n, t= list(map(int, raw_input().split()))
a = list(map(int, raw_input().split()))
 
cont = 0
i = 0

while i < (t-1):
    cont += a[i]
    i += a[i]

if cont == (t-1):
    print "YES"
else:
    print "NO"
