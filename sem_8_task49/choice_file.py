from print_data import print_file #чтоб знать в каком файле что лежит



def choice_number_file():
    print_file()
    number = int(input("Выберите файл\n"
                       "Ведите 1 или 2: "))
    while number <1 or number > 2:
        number = int(input("Ошибка!!!!\n"
                       "Ведите 1 или 2: "))
    return number