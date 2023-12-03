"""Задача №31  Требуется найти N-е число Фибоначчи"""

def fibonacci(n):
    if n < 3:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

# Вычисляем число Фибоначчи для n = 10
n = 7
result = fibonacci(n)
print(f"Число Фибоначчи для n = {n}: {result}")

fib1, fib2 = 0, 1

# через цикл (проще и быстрее)
for i in range(0, n):
    fib1, fib2 = fib2, fib1 + fib2
print(f"{n}-е число Фибоначчи равно {fib2}")
