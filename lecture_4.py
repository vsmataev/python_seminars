# def f(x):
#     return x*x

# print (f(5))

# d=f  # по сути это всего лишь ссылка на область памяти где лежит f(x)
# print(d(5))

# def calc1(a):
#     return a+a

# def calc2(a):
#     return a*a

# def math(op, x):
#     print(op(x))
# math(calc1, 5)  # получится 5

# math(calc2, 5) 

# def math2(op, x, y):
#     print(op(x, y))

# def calc3(x,y):
#     return x+y
# math2(calc3, 6, 4)


# math2(lambda a,b: a + b, 6, 4)  # a и b - это то, что передается в функцию, после двоеточия - то что и с чем нужно с этим делать

"""В списке хранятся числа. Нужно выбрать только чётные числа и составить список пар (число; квадрат числа).
Пример:12358152338 Получить: [(2, 4), (8, 64), (38, 1444)]"""

# тривиальное решение
# data = [1, 2, 3, 5, 8, 15, 23, 38] # тут список()
# out = []
# for i in data :
#     if i % 2 == 0: out.append((i, i ** 2)) # тут кортеж[]
# print(out)

"""через функцию"""
# def select(f, col):
#     return [f(x) for x in col] # ко всем элементам списка применяем функцию  f
# def where(f, col):
#     return [x for x in col if f(x)] # применится ко всем х для которых выполняется условие f(x)

# data = [1, 2, 3, 5, 8, 15, 23, 38] 
# res = select(int, data)
# # lambda будет функцией f - проверит на четность
# res = where(lambda x: x % 2 == 0, res) 
# print(res) # [2, 8, 38]
# # lambda будет функцией f(x) - выведет число и его квадрат
# res = list(select(lambda x: (x, x ** 2), res)) # тоже кортеж[]
# print(res)

"""функция map - применяет указанную функцию к каждому элементу 
итерируемого объекта и возвращает итератор с новыми объектами.
 """

# list_1 = [x for x in range(1, 20)]
# print(list_1)
# list_1 = list(map(lambda x: x+10, list_1))
# print(list_1)

"""Задача: C клавиатуры вводится некий набор чисел, в качестве разделителя используется пробел. 
Этот набор чисел будет считан в качестве строки. Как превратить list строк в list чисел?"""

"решение"

# data = '1 2 3 4 5 6 7 8 9'
# print(data) # 1 2 3 4 5 6 7 8 9 - это строка
# data_1 = data.split() # строка.split() - убирает все пробелы и создает список из значений строки
# print(data_1) # получим список ['1', '2', '3', '4', '5', '6', '7', '8', '9'] - это уже отдельные элементы
# data = list(map(int, data.split()))
# print(data) # это уже числа


"""Функция filter - применятся ко всем объектам, но возвращает только те, для которых значение =true (аналогично where)"""
# data = [x for x in range(10)]
# res = list(filter(lambda x: x % 2 == 0, data)) # отберет только четные числа
# print(res) # [0, 2, 4, 6, 8]

"""Функция zip - возвращает итератор с кортежами из элементов входных данных (списка)
при этом главным является список с МИНИМАЛЬНЫМ количеством"""


users = ['user1', 'user2', 'user3', 'user4', 'user5'] 
ids = [4, 5, 9, 14, 7]
salary = [111, 222, 333] # всего 3 значения
data = list(zip(users, ids, salary))
print(data) # [('user1', 4, 111), ('user2', 5, 222), ('user3', 333)] - в кортеже всего 3 элемента

"""Функция enumerate - Функция enumerate() применяется к итерируемому объекту 
и возвращает новый итератор с кортежами из индекса и элементов входных данных 
(позволяет пронумеровать набор данных.)."""

data = list(enumerate(users))
print(data) # [(0, 'user1'), (1, 'user2'), (2, 'user3))]