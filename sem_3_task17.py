"""Дан список чисел. Определите, сколько в нем
встречается различных чисел."""

# Заданный список чисел
numbers = [1, 2, 3, 4, 2, 3, 5, 6, 7, 1, 4]

# Используем множество для определения уникальных чисел
unique_numbers = set(numbers) # повторов не будет

# Выводим количество уникальных чисел в списке
print("Количество различных чисел в списке:", len(unique_numbers))

"""Этот код создает множество unique_numbers, 
содержащее только уникальные элементы из списка numbers, 
а затем выводит количество этих уникальных чисел 
с помощью функции len(), которая возвращает количество элементов в множестве."""