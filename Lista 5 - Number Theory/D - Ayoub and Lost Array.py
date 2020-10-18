n, l, r = map(int, raw_input().split()) 

mod = 1000000007

aux = [0] * 3
a = [0] * (n+1) 
b = [0] * (n+1)
c = [0] * (n+1)

aux[0] = aux[1] = aux[2] = (r-l+1)/3

if (r-l+1) % 3 == 2:
  aux[1] += 1 
  aux[2] += 1 
elif (r-l+1) % 3 == 1:
  aux[1] += 1 

if l%3 == 2:
  aux = [aux[2], aux[0], aux[1]]
elif l%3==0:
    aux=[aux[1],aux[2],aux[0]] 

c[1] = aux[2]
a[1] = aux[0]
b[1] = aux[1]

for i in range(2, n+1):
  
  a[i]=(a[i-1]*aux[0] + b[i-1]*aux[2] + c[i-1]*aux[1]) % mod
    
  b[i]=(a[i-1]*aux[1] + b[i-1]*aux[0] + c[i-1]*aux[2]) % mod
  
  c[i]=(a[i-1]*aux[2]+ b[i-1]*aux[1] + c[i-1]*aux[0]) % mod 

print a[n] % mods
