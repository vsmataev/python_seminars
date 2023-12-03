
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

# мой вариант

input_list = [{"V":"S001"}, {"V":"S002"}, {"VI":"S001"},
                {"VI":"S005"}, {"VII": "S005"}, 
                {"V":"S009 "}, {"VIII ":"S007"}]

unique_values = set()

for item in input_list:
    for value in item.values():
        unique_values.add(value.strip())  # Добавляем уникальные значения в множество, убирая лишние пробелы

print("Уникальные значения в словаре:")
for value in unique_values:
    print(value)