

def print_file():
    for i in range (1, 3):
        with open(f'python/sem_8_task49/db/data_{i}.txt', 'r', encoding='utf-8') as file:
            data = file.readlines()
        print(f"Вывод данных {i} файла: \n"
              f"{' '.join(data)}") # соеденить (join) все строчки с помошью пустой (' ') строки
       