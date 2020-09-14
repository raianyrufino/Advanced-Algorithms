n = int(raw_input())

coordinates = map(int, raw_input().split())

for i in range(len(coordinates)):
  maximo = 0
  minimo = 0

  if (i != n-1):
    minimo = min(abs(coordinates[i]-coordinates[i+1]),abs(coordinates[i]-coordinates[i-1]))
    
    maximo = max(abs(coordinates[i]-coordinates[0]), abs(coordinates[i]-coordinates[n-1]))
  else:
    minimo = coordinates[n-1]-coordinates[n-2]
    maximo = coordinates[n-1]-coordinates[0]
  
  print minimo, maximo
