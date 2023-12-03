"""Задача №23 Дан массив, состоящий из целых чисел. Напишите
программу, которая подсчитает количество
элементов массива, больших предыдущего (элемента
с предыдущим номером) """

def count_elements_greater_than_previous(arr):
    count = 0
    for i in range(1, len(arr)): # с первого индекса начинаем т.к. индекс 0 не с чем сравнивать
        if arr[i] > arr[i - 1]:  # больше ли текущий элемент, чем предыдущий?
            count += 1
    return count


array = [0, -1, 5, 2, 3]
result = count_elements_greater_than_previous(array)
print("Количество элементов больших предыдущего:", result)