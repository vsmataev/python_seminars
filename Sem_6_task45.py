"""Задача №45.
Два различных натуральных числа n и m называются
дружественными, если сумма делителей числа n
(включая 1, но исключая само n) равна числу m и
наоборот. Например, 220 и 284 – дружественные числа.
По данному числу k выведите все пары дружественных
чисел, каждое из которых не превосходит k. Программа
получает на вход одно натуральное число k, не
превосходящее 10^5
. Программа должна вывести все
пары дружественных чисел, каждое из которых не
превосходит k. Пары необходимо выводить по одной в
строке, разделяя пробелами. Каждая пара должна быть
выведена только один раз (перестановка чисел новую
пару не дает)."""


# семинар

n = int(input("введите число: "))
data = {}
for i in range(2, n + 1):
    summa = 1
    for j in range(2, i // 2 + 1):
        if i % j == 0:
            summa += j
    data[i] = summa
# print(data)
print_list = list()
for k, v in data.items():
    if v in data.keys() and k in data.values() and k != v and data[v] == k and data[k] == v\
        and (k, v) not in print_list:
        print(k, v)
        print_list.append((k, v))

# n = int(input("введите число: "))
# data = {}
# for i in range(2, n + 1):
#     summa = 1
#     for j in range(2, i // 2 + 1):
#         if i % j == 0:
#             summa += j
#     data[i] = summa

# Хранение уже выведенных пар
print_list = []

for k, v in data.items():
    # Проверка на дружественность в одном направлении
    if v in data and k != v and data[v] == k and (k, v) not in print_list: #  выведет в двух направлениях
        print(k, v)
        print_list.append((k, v))




# def sum_of_divisors(n):
#     div_sum = sum(i for i in range(1, n) if n % i == 0)
#     return div_sum

# def friendly_numbers(k):
#     pairs = set()
#     for i in range(1, k + 1):
#         for j in range(i + 1, k + 1):
#             if sum_of_divisors(i) == j and sum_of_divisors(j) == i:
#                 pairs.add((min(i, j), max(i, j)))  # Добавляем во множество, чтобы избежать повторений

#     for pair in pairs:
#         print(*pair)

# k = min(int(input("Введите число k: ")), 10**5)
# friendly_numbers(k)