# Задача №17. 
# Дан список чисел. Определите, сколько в нем
# встречается различных чисел.
# Input: [1, 1, 2, 0, -1, 3, 4, 4]
# Output: 6

list = [1, 1, 2, 0, -1, 3, 4, 4]
print(len(set(list))) # через функцию SET

#   вариант через цикл
list2=[]
for el in list:
    if el not in list2:
        list2.append(el)
print(len(list2))




"""
Задача №19. 
Дана последовательность из N целых чисел и число
K. Необходимо сдвинуть всю последовательность
(сдвиг - циклический) на K элементов вправо, K –
положительное число.
Input: [1, 2, 3, 4, 5] k = 3
Output: [4, 5, 1, 2, 3]
"""

list = [1, 2, 3, 4, 5]
k = 3

new_list = list[k:] + list[:k] # другой вариант через срез
print(new_list)

for i in range(k):
    list.append(list[0])
    list.pop(0)
print(list)

list_1 = [1, 2, 3, 4, 5]
k = 3
print(list_1)
for i in range(k):
    list_1.append(list_1[0])
    list_1.pop(0) 
print(list_1)

list_1 = [1, 2, 3, 4, 5]
new_lst = list_1[k:] + list_1[:k]
print(new_lst)

list_1 = [1, 2, 3, 4, 5]
for i in range(k - 1):
    el = list_1.pop()
    list_1.insert(0, el)
print(list_1)



"""
Задача №21. 
Напишите программу для печати всех уникальных
значений в словаре.
Input: [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"},
{"VI": "S005"}, {"VII": " S005 "}, {" V ":" S009 "}, {" VIII
":" S007 "}]
Output: {'S005', 'S002', 'S007', 'S001', 'S009'}
"""

list_obj = [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"},
         {"VII": " S005 "}, {" V ": " S009 "}, {" VIII": " S007 "}]

my_set = set() # обявляем множество
for el in list_obj:
    for item in el.values():
        my_set.add(item)
print(my_set)

# множественное включение set comrehension
my_set = set(item for el in list_obj for item in el.values())

print(my_set)

"""
Задача №23. 
Дан массив, состоящий из целых чисел. Напишите
программу, которая подсчитает количество
элементов массива, больших предыдущего (элемента
с предыдущим номером)
Input: [0, -1, 5, 2, 3]
Output: 2 (-1 < 5, 2 < 3)
"""

list_nums = [0, -1, 5, 2, 3]
count = 0
for i in range(1, len(list_nums)):
    if list_nums[i] > list_nums[i-1]:
        count +=1
print(count)



"""Задача 10: На столе лежат n монеток. Некоторые из них лежат вверх
решкой, а некоторые – гербом. Определите минимальное число
монеток, которые нужно перевернуть, чтобы все монетки были
повернуты вверх одной и той же стороной. Выведите минимальное
количество монет, которые нужно перевернуть."""

"""через функцию"""

def min_flips(coins):
    heads = sum(1 for coin in coins if coin == 0)
    tails = sum(1 for coin in coins if coin == 1)
    return min(heads, tails)

coins = [0, 1, 1, 0, 0, 1]
min_to_flip = min_flips(coins)
print(min_to_flip)

"""Задача 12: Петя и Катя – брат и сестра. Петя – студент, а Катя –
школьница. Петя помогает Кате по математике. Он задумывает два
натуральных числа X и Y (X,Y≤1000), а Катя должна их отгадать. Для
этого Петя делает две подсказки. Он называет сумму этих чисел S и их
произведение P. Помогите Кате отгадать задуманные Петей числа."""

s = 12
p = 27
for x in range(1, s):  #  от 1 до 12 (сумма)
    y = s - x  # считаем для всех значений
    if x * y == p: # находим условие
        print(x, y)
        found = True # нашел и хватит
        break
