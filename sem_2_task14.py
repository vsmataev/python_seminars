"""Задача 14: Требуется вывести все целые степени двойки (т.е. числа
вида 2k, не превосходящие числа N."""

N = int(input("Введите число N: "))  # Получаем число N от пользователя

power_of_two = 1  # Начинаем с 2^0 = 1

while power_of_two <= N:
    print(power_of_two)  # Выводим текущую степень двойки
    power_of_two *= 2  # Увеличиваем степень двойки на один путем умножения на 2
