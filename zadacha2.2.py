#Задача на if №2

print('Введите три целых числа: ')
#a,b,c = 67, 100, 54
a = int(input())
b = int(input())
c = int(input())

if a < b < c or a > b > c:
    print('Среднее:', b)
elif b < a < c or b > a > c:
    print('Среднее:', a)
else:
    print('Среднее:', c)