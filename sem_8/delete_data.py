from choice_file import choice_number_file

def delete_row():
    nf = choice_number_file()
    with open(f'python/sem_8_task49/db/data_{nf}.txt', 'r', encoding='utf-8') as file:
        data = file.readlines()
    count_rows =  len(data)
    # count_rows = len(file.readlines())
    if count_rows == 0:
        print("Файл пуст!")
    else:
        number_row = int(input(f"Укажите номер строки"
                               f"от 1 до  {count_rows}: "))
        while number_row < 1 or number_row > count_rows:
            number_row = int(input(f"Ошибка! "
                                   f"Укажите номер строки"
                                   f"от 1 до  {count_rows}: "))
        del data[number_row - 1]
        data = [f'{i + 1};{data[i].split(";")[1]};'
               f'{data[i].split(";")[2]};'
               f'{data[i].split(";")[3]};'
               f'{data[i].split(";")[4]}'
               for i in range(len(data))]
        
        with open(f'python/sem_8_task49/db/data_{nf}.txt', 'w', encoding='utf-8') as file:
            file.writelines(data)

        print("Строка удалена")