
#Задачи на if
#№ 1
#a, b, c = 10, 12, 10
print('Введите длину сторон треугольника:')
a, b, c = int(input()), int(input()), int(input()) # решил попробовать записать переменные используя "input"
# в строчку, чтобы проверить, будет ли программа так работать.
# Вопрос: лучше все же как во второй задаче в столбик писать или разницы нет?

if a == b and b == c:
    print('Равносторонний')
elif a == b and b != c or a != b and b == c or a == c and c != b:
    print('Равнобедренный')
elif a != b and b != c and c != a:
    print('Разносторонний')


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


# Задача на if №3
print('Введите название двух цветов из перечисленных, для смешивания: красный, синий, желтый')
a = input(str())
b = input(str())



if a == 'красный' and b == 'синий':
    print('Фиолетовый')
elif a == 'красный' and b == 'желтый':
    print('Оранжевый')
elif a == 'синий' and b == 'желтый':
    print('Зеленый')
else:
    print('Ошибка, введены неверные данные!')

# как при получении ошибки вернуть программу повторно к первой строке, с просьбой ввести названия цветов?




# ЗАДАЧИ НА For:
# Задача №1

# print('Введите целое число: ')
# n = int(input())
# for i in range(n, 0, -1):
#     j = '*'
#     print(j * i)



# Задача №2
# a,b,c,d = 3,10,2,8
#
# print('', end='\t')
# for i in range(c, d + 1):
#     print(i, end='\t')
# print('')
# for j in range(a, b + 1):
#     print(j, end='\t')
#     for k in range(c, d + 1):
#         print(f'{j * k}', end='\t')
#     print('')


# Задача №3

print('Введите целое число: ')
n = int(input())

count = 0
for i in range(1, n + 1):
    for j in range(i):
        count += 1
        print(count, end='')
    print('')
