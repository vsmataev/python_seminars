"""Задача №33. Решение в группах
Хакер Василий получил доступ к классному журналу и
хочет заменить все свои минимальные оценки на
максимальные. Напишите программу, которая
заменяет оценки Василия, но наоборот: все
максимальные – на минимальные."""

# пример кода
new_list = [i for i in range(5)] # можно указывать разные параметры для i ([i if i % 2 == 0 else 1 for i in range(5)])
print(new_list)
new_list.clear()
for i in range(5):
    new_list.append(i)
print(new_list)

# решение задачи (параллельно пример работы list compreheension)

n = int(input("Ведите количество оценок: "))
marks = [int(i) for i in input("введите оценки: ").split()][:n]
print(marks)
print(*[min(marks) if i == max(marks) else i for i in marks]) # максимальное значение в списке заменяется на минимальное

"""Этот код выполняет следующее:

n = int(input("Введите количество оценок: ")) 
запрашивает у пользователя ввести количество оценок и сохраняет 
это значение в переменной n как целое число.

marks = [int(i) for i in input("Введите оценки: ").split()][:n] 
запрашивает у пользователя ввести оценки через пробел и разбивает 
введенную строку на отдельные значения с помощью метода split(). 
Затем он преобразует каждое значение в целое число с помощью 
генератора списка [int(i) for i in ...]. 
Наконец, он выбирает только n первых значений оценок, используя срез [:n] и сохраняет их в список marks.

print(marks) выводит исходный список оценок.

print(*[min(marks) if i == max(marks) else i for i in marks]) 
создает новый список, в котором заменяет максимальное значение оценки 
на минимальное значение. Для этого используется генератор списка, 
который проходит по каждому элементу в списке marks. 
Если элемент равен максимальному значению в списке, 
то в новом списке он заменяется на минимальное значение; 
в противном случае он остается неизменным. Функция min() и max() 
используются для поиска минимального и максимального значений в списке marks.
"""