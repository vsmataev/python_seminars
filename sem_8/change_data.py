from choice_file import choice_number_file


def change_row():
    nf = choice_number_file()
    # file_path = f'python/sem_8_task49/db/data_{nf}.txt' # так тоже можно
    with open(f'python/sem_8/db/data_{nf}.txt', 'r', encoding='utf-8') as file:
        data = file.readlines()
    count_rows =  len(data)
    
    number_row = int(input(f"Укажите номер строки"
                           f"от 1 до  {count_rows}: "))
    while number_row < 1 or number_row > count_rows:
            number_row = int(input(f"Ошибка! "
                                   f"Укажите номер строки"
                                   f"от 1 до  {count_rows}: "))
    
    name = input("введите имя: ")
    surename = input("введите фамилию: ")
    birthdate =input("введите дату рождения дд.мм.гггг: ")
    town = input("укажите город: ")
    data[number_row - 1] = f'{number_row}; {name}; {surename}; {birthdate}; {town}\n'
    # data[number_row - 1] = data[:number_row] + [f'{number_row}; {name}; {surename}; {birthdate}; {town}\n'] + data[number_row:]
    
    with open(f'python/sem_8/db/data_{nf}.txt', 'w', encoding='utf-8') as file:
        file.writelines(data)
    print ("Данные изменены")
   


