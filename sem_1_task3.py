"""Задача №3. В некоторой школе решили набрать три новых
математических класса и оборудовать кабинеты для
них новыми партами. За каждой партой может сидеть
два учащихся. Известно количество учащихся в
каждом из трех классов. Выведите наименьшее
число парт, которое нужно приобрести для них."""

print("количество учащихся в первом классе?")
a = int(input())
print("количество учащихся во втором классе?")
b = int(input())
print("количество учащихся в третьем классе?")
c = int(input())

desks_for_class1 = (a + 1) // 2  # +1 для округления вверх
desks_for_class2 = (b + 1) // 2
desks_for_class3 = (c + 1) // 2
total_desks = desks_for_class1 + desks_for_class2 + desks_for_class3

print("минимальное количество парт - ", total_desks)