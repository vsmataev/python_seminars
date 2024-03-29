"""Задача 28: Напишите рекурсивную функцию sum(a, b),
возвращающую сумму двух целых неотрицательных чисел. Из
всех арифметических операций допускаются только +1 и -1.
Также нельзя использовать циклы."""

def sum(a, b):
    if a == 0:
        return b
    return sum(a - 1, b + 1)

# складывает числа a и b, 
# уменьшая a и увеличивая b на единицу, 
# пока a не станет равным нулю. Когда a достигнет нуля, 
# функция вернет значение b, которое будет суммой исходных чисел a и b
a = 3
b = 5
print(sum(a, b))