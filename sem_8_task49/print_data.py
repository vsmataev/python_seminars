def print_file():
    for i in range (1, 3):
        with open (f'db/data_{i}.txt', 'r', encoding='utf-8') as file:
            data = file.readlines()
        print(f"Выводданных {i} файла: \n"
              f"{data}")
        
print_file()