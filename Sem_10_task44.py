"""Задача 44: В ячейке ниже представлен код генерирующий DataFrame,
которая состоит всего из 1 столбца. Ваша задача перевести его в one hot вид.
Сможете ли вы это сделать без get_dummies?"""

# Решение

import pandas as pd
import random

lst = ['robot'] * 10
lst += ['human'] * 10
random.shuffle(lst)
data = pd.DataFrame({'whoAmI' : lst})
data.head()
print(data)
unique_values = data['whoAmI'].unique()

# Создание нового DataFrame, везде 0
one_hot_data = pd.DataFrame(0, columns=unique_values, index=range(len(data)))

# Проход по строкам и установка 1 для соответствующего столбца
for ind, val in enumerate(data['whoAmI']):
    one_hot_data.iloc[ind, one_hot_data.columns.get_loc(val)] = 1

one_hot_data2 = pd.get_dummies(data['whoAmI'])
print(one_hot_data)
print(one_hot_data2)

