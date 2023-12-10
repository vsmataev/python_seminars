from choice_file import choice_number_file



def add_row():
    nf = choice_number_file()
    name = input("введите имя: ")
    surename = input("введите фамилию: ")
    birthdate =input("введите дату рождения дд.мм.гггг: ")
    town = input("укажите город: ")

    with open(f'python/sem_8_task49/db/data_{nf}.txt', 'r', encoding='utf-8') as file:
        data = file.readlines() # список всех строк нашего файла
        now_number_row = len(data) + 1 # узнаем количество строк, добавим 1 и узнаем какая строка следующая

    with open(f'python/sem_8_task49/db/data_{nf}.txt', 'a', encoding='utf-8') as file:
        file.write(f'{now_number_row}; {name}; '
                   f'{surename}; {birthdate}; {town}\n')
    print("Данные успешно добавлены")
