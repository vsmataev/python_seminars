'''
Создать телефонный справочник с возможностью импорта и экспорта данных в
формате .txt. Фамилия, имя, отчество, номер телефона - данные, которые должны находиться
в файле.
1. Программа должна выводить данные
2. Программа должна сохранять данные в текстовом файле
3. Пользователь может ввести одну из характеристик для поиска определенной
записи(Например имя или фамилию человека)
4. Использование функций. Ваша программа не должна быть линейной
'''

"Ветка REQUEST создана для pull-request-a"

import os
from csv import DictReader, DictWriter



class LenNumberError(Exception):
    def __init__(self, txt):
        self.txt = txt

class NameError(Exception):
    def __init__(self, txt):
        self.txt = txt

def get_info():
    is_valid_first_name = False
    while not is_valid_first_name:
        try:
            first_name = input("Введите имя: ")
            if len(first_name) == 0:
                raise NameError("Поле 'имя' не может быть пустым ")
            else:
                is_valid_first_name = True
        except NameError as err:
            print(err)
            continue

    is_valid_last_name = False
    while not is_valid_last_name:
        try:
            last_name = input("Введите фамилию: ")
            if len(last_name) == 0:
                raise NameError("Фамилия должна быть заполнена")
            else:
                is_valid_last_name = True
        except NameError as err:
            print(err)
            continue

    is_valid_phone = False
    while not is_valid_phone:
        try:
            phone_number = int(input("Введите номер: "))
            if len(str(phone_number)) != 11:
                raise LenNumberError("Неверная длина номера")
            else:
                is_valid_phone = True
        except ValueError:
            print("Не валидный номер!!!")
            continue
        except LenNumberError as err:
            print(err)
            continue

    return [first_name, last_name, phone_number]


def create_file(file_name):
    folder_path = 'python/Task_49_phones'
    file_path = os.path.join(folder_path, file_name)
    if not os.path.exists(file_path):
        with open(file_path, "w", encoding='utf-8') as data:
            f_writer = DictWriter(data, fieldnames=['Имя', 'Фамилия', 'Телефон'])
            f_writer.writeheader()


def write_file(file_name, lst):
    with open(file_name, "r", encoding='utf-8') as data:
        res = list(DictReader(data))

    for el in res:
        if el["Телефон"] == str(lst[2]):
            print("Такой телефон уже есть")
            return

    obj = {"Имя": lst[0], "Фамилия": lst[1], "Телефон": lst[2]}
    res.append(obj)

    with open(file_name, "w", encoding='utf-8', newline='') as data:
        fieldnames = ['Имя', 'Фамилия', 'Телефон']
        f_writer = DictWriter(data, fieldnames=fieldnames)
        f_writer.writeheader()
        f_writer.writerows(res)


def get_csv_files():
    folder_path = os.path.join('python', 'Task_49_phones')
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)
    files = [f for f in os.listdir(folder_path) if f.endswith('.csv')]
    return [os.path.join(folder_path, f) for f in files]


def display_file_content(file_index, files=None):
    if files:
        file_name = files[file_index - 1]
    else:
        file_name = file_index

    try:
        with open(file_name, "r", encoding='utf-8') as data:
            lines = data.readlines()[1:]  # Пропускаем первую строку
            for i, line in enumerate(lines, 1):
                print(f"{i}. {line.strip()}")
    except FileNotFoundError:
        print("Файл отсутствует.")


def copy_lines(files, source_index, destination_index, line_number):

    destination_file = None  # Создаем переменную для записи названия файла назначения

    try:
        if 0 < source_index <= len(files) and 0 < destination_index <= len(files):
            source_file = files[source_index - 1]
            destination_file = files[destination_index - 1]
            with open(source_file, 'r', encoding='utf-8') as source:
                lines = source.readlines()[1:]  # Пропуск первой строки

            if 0 < line_number <= len(lines):
                line_to_copy = lines[line_number - 1]
                with open(destination_file, 'a', encoding='utf-8') as destination:
                    destination.write(line_to_copy)

                print(f"Строка {line_number} из {source_file} успешно скопирована в {destination_file}")
            else:
                print("Ошибка: Некорректный номер строки.")
        else:
            print("Ошибка: Некорректный номер файла.")
    except FileNotFoundError:
        print("Ошибка: Один из файлов не найден.")


def search_by_name_or_lastname(file_index, files, keyword):
    if 0 < file_index <= len(files):
        file_name = files[file_index - 1]
        with open(file_name, "r", encoding='utf-8') as data:
            reader = DictReader(data)
            found_entries = []
            for i, entry in enumerate(reader, 1):
                if keyword.lower() in entry["Имя"].lower() or keyword.lower() in entry["Фамилия"].lower():
                    entry["Номер строки"] = i
                    found_entries.append(entry)
            return found_entries
    else:
        print("Некорректный номер файла.")
        return []


def main():
    files = []

    while True:
        files = get_csv_files()

        if not files:
            print("Нет доступных CSV файлов.")
            create_new_file = input("Хотите создать новый файл? (yes/no): ")
            if create_new_file.lower() == 'yes':
                new_file_name = input("Введите имя нового файла: ")
                create_file(new_file_name + '.csv')
            else:
                break

        print("Доступные CSV файлы:")
        for i, file in enumerate(files, 1):
            print(f"{i}. {file}")

        file_choice = input("Выберите файл (введите номер)\n"
                    "или создайте новый - 'n' \n"
                    "'q' для выхода): ")

        if file_choice.lower() == 'q':
            break
        elif file_choice.lower() == 'n':
            new_file_name = input("Введите имя нового файла: ")
            create_file(new_file_name + '.csv')
            print(f"Файл {new_file_name}.csv создан.")
            continue

        if file_choice.lower() == 'q':
            break
        elif file_choice.lower() == 'n':
            new_file_name = input("Введите имя нового файла: ")
            create_file(new_file_name + '.csv')
            print(f"Файл {new_file_name}.csv создан.")
            continue

        try:
            file_index = int(file_choice) - 1
            if 0 <= file_index < len(files):
                selected_file = files[file_index]
                print(f"Выбран файл: {file_index + 1}")
            while True:
                command = input("Выберите команду: \n"
                        "l. Просмотреть содержимое \n"
                        "w. Добавить контакт\n"
                        "f. поиск контактов \n"
                        "c. скопировать данные из одного файла в другой\n"
                        "q. выход\n"
                        "Введите команду: ")
                if command == 'q':
                         break
                elif command == 'l':
                 display_file_content(selected_file)
                elif command == 'w':
                 write_file(selected_file, get_info())
                 display_file_content(selected_file)
                elif command == 'c':
                        source_index = int(input("Введите номер файла, из которого нужно скопировать строки: ")) - 1
                        selected_file = files[source_index]
                        display_file_content(selected_file)  # Вывод содержимого выбранного файла

                        destination_index = int(input("Введите номер файла, в который нужно скопировать строки: ")) - 1
                        line_number = int(input("Введите номер строки для копирования: "))
                        copy_lines(files, source_index + 1, destination_index + 1, line_number)
                        selected_file = files[destination_index]
                        display_file_content(selected_file)
                elif command == 'f':
                        keyword = input("Введите имя или фамилию: ")
                        file_choice = int(file_choice)
                        found_entries = search_by_name_or_lastname(file_choice, files, keyword)
                        if found_entries:
                                print("Найденные записи:")
                                for entry in found_entries:
                                    print(f"Номер строки в исходном файле: {entry['Номер строки']}, {entry['Имя']}, {entry['Фамилия']}, Телефон: {entry['Телефон']}")
                        else:
                            print("Ничего не найдено.")
        
      
        except ValueError:
             print("Введите корректный номер файла")

if __name__ == "__main__":
    main()