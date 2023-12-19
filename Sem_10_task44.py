"""Задача 44: В ячейке ниже представлен код генерирующий DataFrame,
которая состоит всего из 1 столбца. Ваша задача перевести его в one hot вид.
Сможете ли вы это сделать без get_dummies?"""

import pandas as pd
import random

lst = ['robot'] * 10
lst += ['human'] * 10
random.shuffle(lst)
data = pd.DataFrame({'whoAmI':lst})
data.head()

unique_values = data['whoAmI'].unique()

# Создание пустого DataFrame
one_hot_data = pd.DataFrame(0, columns=unique_values, index=range(len(data)))

# Проход по строкам и установка 1 для соответствующего столбца
for ind, val in enumerate(data['whoAmI']):
    one_hot_data.loc[ind, val] = 1

print(one_hot_data.head())