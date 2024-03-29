"""Задача №35.
Напишите функцию, которая принимает одно число и
проверяет, является ли оно простым
Напоминание: Простое число - это число, которое
имеет 2 делителя: 1 и n(само число)"""

def prime_check(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):  # проверяем делители от 2 до корня из n (если не найдены, то n простое)
        if n % i == 0:
            return False
    return True

number = 17
if prime_check(number):
    print(f"{number} - простое число")
else:
    print(f"{number} - не простое число")