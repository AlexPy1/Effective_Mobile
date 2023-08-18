def add_number(first_name, last_name, surname, organization_name, work_phone, personal_phone):
    # Функция для добавления новой строки в телефонный справочник
    with open("phonebook.txt", 'a', encoding='UTF-8') as phonebook:
        phonebook.write(f"first_name: {first_name} last_name: {last_name} surname: {surname} "
                        f"organization_name: {organization_name} work_phone: {work_phone} "
                        f"personal_phone: {personal_phone}")
        phonebook.write('\n')
        print(f'New line append! {first_name, last_name, surname, organization_name, work_phone, personal_phone}\n')
        return


def print_numbers():
    # Функция, выводящая все имеющиеся в файле номера
    with open("phonebook.txt", encoding='UTF-8') as phonebook:
        cnt = 0
        for line in phonebook:
            if cnt < 10:
                print(line.strip())
                cnt += 1
            else:
                a = input('Следующая страница введите 1\n'
                          'Для выхода введите q: ')
                if a == 'q':
                    return
                elif a == '1':
                    print(line.strip())
                    cnt = 1
    print('')


def search_number(first_name=None, last_name=None, surname=None, organization_name=None, work_phone=None,
                  personal_phone=None):
    # Функция для поиска номера телефона по переданному параметру
    with open("phonebook.txt", encoding='UTF-8') as phonebook:
        flag = False
        for line in phonebook:
            line = line.split()
            if first_name in line or last_name in line or surname in line or organization_name in line or \
                    work_phone in line or personal_phone in line:
                print(*line)
                flag = True
    if not flag:
        print('Не найдено. Проверьте корректность данных\n')
    else:
        print("")


def refactor_line(first_name=None, last_name=None, surname=None, organization_name=None, work_phone=None,
                  personal_phone=None):
    # Функция для редактирования записи
    with open("phonebook.txt", encoding='UTF-8') as phonebook:
        for line in phonebook:
            line_list = line.split()
            if first_name in line_list or last_name in line_list or surname in line_list or organization_name in line_list or \
                    work_phone in line_list or personal_phone in line_list:
                print(line)
                flag = input('Вы хотите изменить эту строку?\n 1 - да\n 2 - нет: ')
                if flag == '1':
                    print('Введите новые данные')
                    first_name = input('Введите фамилию: ')
                    last_name = input('Введите имя: ')
                    surname = input('Введите отчество: ')
                    organization_name = input('Введите название компании: ')
                    work_phone = input('Введите рабочий номер: ')
                    personal_phone = input('Введите личный номер: ')
                    try:
                        with open('phonebook.txt', 'r', encoding='UTF-8') as f:
                            old_data = f.read()
                            data = f"first_name: {first_name} last_name: {last_name} surname: {surname} " \
                                   f"organization_name: {organization_name} " \
                                   f"work_phone: {work_phone} personal_phone: {personal_phone} \n"
                            new_data = old_data.replace(line, data)
                        with open('phonebook.txt', 'w', encoding='UTF-8') as f:
                            f.write(new_data)
                            print("Данные изменены")
                            return
                    except:
                        print(
                            'Передано не полное количество полей. Пожалуйста, проверьте корректность передаваемых данных')
                elif flag == '2':
                    continue
    print('Не найдено\n')


def main():
    while True:
        a = input('Для вывода всех записей введите 1\n'
                  'Для добавления новой записи введите 2\n'
                  'Для редактирования записи введите 3\n'
                  'Для поиска записи введите 4\n'
                  'Для выхода введите q: ')
        if a == 'q' or a == 'й':
            return
        elif a == '1':
            print_numbers()
        elif a == '2':
            first_name = input('Введите фамилию: ')
            last_name = input('Введите имя: ')
            surname = input('Введите отчество: ')
            organization_name = input('Введите название компании: ')
            work_phone = input('Введите рабочий номер: ')
            personal_phone = input('Введите личный номер: ')
            add_number(first_name, last_name, surname, organization_name, work_phone, personal_phone)
        elif a == '3':
            first_name = input('Введите фамилию: ')
            last_name = input('Введите имя: ')
            surname = input('Введите отчество: ')
            organization_name = input('Введите название компании: ')
            work_phone = input('Введите рабочий номер: ')
            personal_phone = input('Введите личный номер: ')
            refactor_line(first_name, last_name, surname, organization_name, work_phone, personal_phone)
        elif a == '4':
            first_name = input('Введите фамилию: ')
            last_name = input('Введите имя: ')
            surname = input('Введите отчество: ')
            organization_name = input('Введите название компании: ')
            work_phone = input('Введите рабочий номер: ')
            personal_phone = input('Введите личный номер: ')
            search_number(first_name, last_name, surname, organization_name, work_phone, personal_phone)
        else:
            print("Неизвестная команда\n")


main()
