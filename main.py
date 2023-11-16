# print(5,6,7,8,9)

# n=5
# print(n)
# print(type(n))
# n = 'test'

# # print(n)
# n1 = "test2"

# a=5
# b=5.8
# c='hello'
# print(f"{a} - {b} - {c}")
# print("{} - {} - {}" .format(a,b,c)) # типы вывода

# print("введите первое число")
# a=input()
# b=input(" введите второе число") # число введется в этой же строке
# print(a)

# print(a, '+', b, '=', a+b) # результатом будет сложение строк, а не чисел - ab


# print("введите первое число")
# a=int(input())
# b=int(input(" введите второе число")) # число введется в этой же строке

print(a, '+', b, '=', a+b) # теперь верно


 #Найдите сумму цифр трехзначного числа n.
# Результат сохраните в перменную res.

a=4.5786
b=3.567123
print(a*b)
print(round(a*b, 3)) # округлит до третьего знака

 
res = 0
 
while n > 0:
    digit = n % 10
    res = res + digit
    n = n // 10
 
print("Сумма:", res)

# Петя, Катя и Сережа делают из бумаги журавликов. Вместе они сделали n журавликов.
# Сколько журавликов сделал каждый ребенок, если известно, что Петя и Сережа сделали 
# одинаковое количество журавликов, а Катя сделала в два раза больше журавликов, 
# чем Петя и Сережа вместе?
# Выведите через пробел количество журавликов, сделанных Петей, Катей и Сережей.

# задача про фибоначи

A = int(input("Введите число: "))

f1 = 0
f2 = 1
f3 = 1
i = 2
while f3 <= A:
    i = i + 1
    f3 = f2 + f1
    if f3 == A:
        print(f"{A} - {i} - ое число Фибоначчи")
        break
    f1 = f2
    f2 = f3
    print(f3)
else:
    print(-1)

    # задача про погоду
    import random
n = int(input())
sundays0 = 0
sundaysmax = 0
for day in range(n):
    temp = random.randint(-50, 50)
    print(temp)
    if temp > 0:
        sundays0 +=1
    else:
        sundays0 = 0
    if sundays0 > sundaysmax:
        sundaysmax = sundays0

print(sundaysmax)

# другой вариант
n = 6
count = 0
count_final = 0
for i in range(n):
    temper = int(input(f'Введите среднесуточную температуру {i + 1} дня '))
    if temper > 0:
        count += 1
    else:
        count = 0
    if count_final < count:
        count_final = count
print(f'Самая длинная оттепель {count_final} дней')

# задача про арбузы (самый легкий и самый тяжелый)

from random import randint
n = int(input('Введите количество арбузов: '))
watermelons = []
for i in range(n):
    watermelons.append(randint(1, 100)) # наполняем массив элементами от 1 до 99
print(watermelons)
print(f"Минимальный арбуз {min(watermelons)}")
print(f"Максимальный арбуз {max(watermelons)}")

r = randint(1, 100)
print(f"Рандомное число r - {r}")

# вариант 2

import random
number = int(input())
mass = []
for arbus in range(number):
    mass.append(random.randint(1,10))
    
print(min(mass), max(mass))
