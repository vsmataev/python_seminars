"""Задача 30: Заполните массив элементами арифметической
прогрессии. Её первый элемент, разность и количество
элементов нужно ввести с клавиатуры. Формула для
получения n-го члена прогрессии: a
n= a1+ (n-1) * d.
Каждое число вводится с новой строки."""

a1 = int(input("Введите первый элемент: "))
d = int(input("Введите разность: "))
n = int(input("Введите количество элементов: "))

# Инициализация массива
progression = []

# Заполнение массива
for i in range(n):
    an = a1 + i * d  # Формула для вычисления n-го члена прогрессии
    progression.append(an)

# Вывод прогрессии
print("Арифметическая прогрессия:")
for number in progression:
    print(number)