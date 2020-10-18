n, m = map(int, raw_input().split())
cont = 0

while m>n:
    if (m%2) == 0:
        m = m / 2
    else:
        m += 1

    cont += 1 

print cont + (n-m)
