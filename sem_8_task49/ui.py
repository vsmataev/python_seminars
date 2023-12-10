from delete_data import delete_row
from change_data import change_row
from add_data import add_row
from print_data import print_file


def check_number(n): # проверка правильности ввода
    while n < 1 or n > 5:
       n = int(input("Ошибка, такого номера команды не "
                     "существует! Ведите цифру от 1 до 5\n"
                     "выберите функцию: \n"
                     "1. Добавить\n"
                     "2. Удалить\n"
                     "3. Изменить\n"
                     "4. Вывод\n"
                     "5. Выход\n"
                     "Введите номер команды: "))
    return n
       



def start_menu():
    command = None # пустое значение
    while command != 5:
        command = int(input("Здравствуйте!\n"
                        "выберите функцию: \n"
                        "1. Добавить\n"
                        "2. Удалить\n"
                        "3. Изменить\n"
                        "4. Вывод\n"
                        "5. Выход\n"
                        "Введите номер команды: "))

   
    # while command != 5:
        command = check_number(command)
        if command == 1:
            add_row()
        elif command == 2:
            delete_row()
        elif command == 3:
            change_row()
        elif command == 4:
            print_file()

        command = check_number(command)  # Обновляем значение command после выполнения каждой команды

    print("всем спасибо! до свидания")
