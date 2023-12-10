"""Задача №51. Решение в группах
Напишите функцию 

same_by(characteristic, objects), 

которая проверяет, все ли объекты имеют одинаковое значение некоторой характеристики, 
и возвращают True, если это так. Если значение характеристики для разных объектов
отличается - то False. Для пустого набора объектов, функция должна возвращать True. Аргумент characteristic - это
функция, которая принимает объект и вычисляет его характеристику."""

values = [2, 4, 4, 3]

def same_by (characteristic, objects):
    
    for i in objects:
        if characteristic(i) != True:
            return False
    return True

if same_by(lambda x: x % 2 == 0, values):
    print("same")
else:
    print("different")