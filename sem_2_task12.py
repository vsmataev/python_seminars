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
