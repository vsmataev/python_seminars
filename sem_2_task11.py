"""Задача №11. Решение в группах
Дано натуральное число A > 1. Определите, каким по
счету числом Фибоначчи оно является, то есть
выведите такое число n, что φ(n)=A. Если А не
является числом Фибоначчи, выведите число -1."""

a = 5
fib_prev, fib_next = 0, 1
count = 2
while a > fib_next:
    fib_prev, fib_next = fib_next, fib_prev + fib_next
    count += 1
if a == fib_next:
    print(count)
else:
    print('-1')

    # другой вариант
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