def find_error_solucionated(erros, aux):
  value = 0
  j = 0
  while(j < len(aux) and value == 0):
    if(erros[j] != aux[j]):
      value = erros[j]
    j+= 1
  
  if(value == 0):
    value = erros[j]

  return value

n = int(raw_input())

errors_first_time = sorted(list(map(int, raw_input().split())))
errors_second_time = sorted(list(map(int, raw_input().split())))
errors_third_time = sorted(list(map(int, raw_input().split())))

print find_error_solucionated(errors_first_time, errors_second_time)
print find_error_solucionated(errors_second_time, errors_third_time)
