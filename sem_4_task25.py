"""Задача №25. 
Напишите программу, которая принимает на вход строку, и отслеживает, сколько раз каждый символ
уже встречался. Количество повторов добавляется к символам с помощью постфикса формата _n.
Input: a a a b c a a d c d d
Output: a a_1 a_2 b c a_3 a_4 d c_1 d_1 d_2
Для решения данной задачи используйте функцию
.split()"""

def track_character_occurrences(input_string):
    words = input_string.split()
    occurrences = {} # словарь

    result = [] # будет список строк
    for word in words:
        if word in occurrences:
            occurrences[word] += 1
            result.append(f"{word}_{occurrences[word]}") # f-строка
        else:
            occurrences[word] = 0 # значения начинаются с 0
            result.append(word)
    print(occurrences) # {'a': 4, 'b': 0, 'c': 1, 'd': 2}
    return ' '.join(result) 

# Заданная строка
input_str = "a a a b c a a d c d d"

# Вызов функции для отслеживания встречаемости символов
output_str = track_character_occurrences(input_str)
print(output_str)  # a a_1 a_2 b c a_3 a_4 d c_1 d_1 d_2

# вариант с семинара (вывод напрямую в процессе обхода)
list = "a a a b c a a d c d d".split()
print(list)
dct={}
for item in list:
    if item in dct:
        print(f'{item}_{dct[item]}', end=' ')
    else:
        print(item, end=" ")  # end= значит что вывод продолжается в этой же строке
        # все значения начинаются с 1 
    dct[item] = dct.get(item, 0) +1 
print(dct) # {'a': 5, 'b': 1, 'c': 2, 'd': 3}