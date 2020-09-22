n, m = map(int, raw_input().split())

matrix_row = [0] * 100001
matrix_col = [0] * 100001

row = 0
col = 0

cont = n*n

for i in range(m):
  x, y = map(int, raw_input().split())

  if matrix_row[x-1] == 0:
    matrix_row[x-1] = 1
    cont -= (n - col)
    row +=1
  
  if matrix_col[y-1] == 0:
    matrix_col[y-1] = 1
    cont -= (n-row)
    col += 1
   
  print cont
