#Сафиуллина Арина ИВТ 2 курс
#Вычислите сумму цифр данного натурального числа. 
def function():
  c=input('Введите натуральное число:')
  return c
def summa(c):
  list1=list(c) 
  sum=0
  for l in list1 : 
    sum=sum+ int(l) 
  return sum
def result(out):
  print('Сумма данного натурального числа: {}'.format(out))
  return out

result(summa(function()))
