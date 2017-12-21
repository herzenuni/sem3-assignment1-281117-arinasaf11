#Сафиллина Арина ИВТ 2 курс
#Найдите все двузначные и трехзначные числа, сумма квадратов цифр которых делится на 17. 
def function2(с):
  str1=str(с)
  sum=0
  for s in str:
      ch=int(s)
      sum+=ch**2
  return sum 

def func():
  for i in range(10, 100): #двухзначные числа
    if function2(i) % 17 == 0:
      print('Двузначное число: {}'.format(i))  
  for i in range(100, 1000): #трехзначные числа
    if function2(i) % 17 == 0:
      print('Трехзначное число: {}'.format(i))
      
func()     
