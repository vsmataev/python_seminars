"""Задача №43.
Дан список чисел. Посчитайте, сколько в нем пар
элементов, равных друг другу. Считается, что любые
два элемента, равные друг другу образуют одну пару,
которую необходимо посчитать. Вводится список
чисел. Все числа списка находятся на разных
строках."""

# решение через словарь

numbers = [int(i) for i in input("введите числа ").split()] # 2 33 4 2 33 4  5  55 
count_numbers = {}

for i in numbers:
    if i not in count_numbers: # count_numbers.keys()
        count_numbers[i] = 1 # 1 т.к. одно число (первое) уже встретилось
    else: # i является ключем
        count_numbers[i] += 1
print(count_numbers)
print(sum([i // 2 for i in count_numbers.values()])) # находит количество пар чисел, разделив значение для каждого числа на 2 и складывая эти частные
# for num in numbers:
#     count_numbers[num] = count_numbers.get(num, 0) + 1

# print(count_numbers) # {2: 2, 33: 2, 4: 2, 5: 1, 55: 1}