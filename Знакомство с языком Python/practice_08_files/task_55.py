"""
Задача №55. Создать телефонный справочник с возможностью импорта и экспорта данных в формате .txt. Фамилия, имя,
отчество, номер телефона - данные, которые должны находиться в файле.
Программа должна выводить данные
Программа должна сохранять данные в текстовом файле
Пользователь может ввести одну из характеристик для поиска определенной записи(Например имя или фамилию человека)
Использование функций. Ваша программа не должна быть линейной
"""

"""
План действий:
1. Создание файла
    1.1 Открываем файл на дозапись
2. Запись данных в файл
    2.1 Получить от пользователя контакт
    2.2 Открыть файл на дозапись
    2.3 Записать данные
3. Вывод данных на экран
    3.1 Открыть файл на чтение
    3.2 Получаем данные из файла
    3.3 Выводим данные на экран
4. Поиск контакта
    4.1 запрос варианта поиска контакта
    4.2 Получить от пользователя контакт, который будем искать
    4.3 Открываем файл на считывание
    4.4 Получаем данные из файла
    4.5 Осуществляем поиск контакта
    4.6 вывод контакта на экран
5. Создание интерфейса
    5.1 вывести меню на экран
    5.2 запрос действия
    5.3 запуск соответсвующей функции
    5.4 выход из программы
6. Копирование даных в новый файл
    6.0 Чтение файла и получение данных
    6.1 запрос на ввод номера строки для копирования
    6.2 Получение контакта, который будет скопирован
    6.3 Запрос имени файла, куда будут скопированы данные
    6.4 Записываем данные в файл     
"""


def input_surname():
    return input('Введите фамилию: ').title()


def input_name():
    return input('Введите имя: ').title()


def input_patronumic():
    return input('Введите отчество: ').title()


def input_phone():
    return input('Введите телефон: ')


def input_address():
    return input('Введите адрес: ').title()


def create_contact():
    surname = input_surname()
    name = input_name()
    patronomic = input_patronumic()
    phone = input_phone()
    address = input_address()
    return f'{surname} {name} {patronomic} {phone}\n{address}'


def data_input():
    contact = create_contact()
    with open('phonebook.txt', 'a', encoding='utf-8') as file:
        file.write(f'{contact}\n\n')


def read_file():
    with open('phonebook.txt', 'r', encoding='utf-8') as file:
        return file.read()


def print_data():
    contacts = read_file()
    contacts_list = contacts.strip().split('\n\n')
    for contact in enumerate(contacts_list, 1):
        print(*contact)
    print()


def search_contact():
    print('Варианты поиска:\n'
          '1 - по фамилии\n'
          '2 - по имени\n'
          '3 = по отчеству\n'
          '4 - по телефону\n'
          '5 - по городу\n')

    var = input('Вибирете необходимый вариант: ')
    while var not in ['1', '2', '3', '4', '5']:
        print('Не корректный ввод данных!')
        var = input('Выберите действие: ')
        print()

    i_var = int(var) - 1

    search = input('Введите данные для поиска: ').title()
    print()
    contacts = read_file()
    contacts_list = contacts.strip().split('\n\n')
    for contacts_str in contacts_list:
        contacts_lst = contacts_str.replace('\n', ' ').split()
        if search.title() in contacts_lst[i_var]:
            print(contacts_str)
    print()


def interface():
    with open('phonebook.txt', 'a', encoding='utf-8'):
        pass

    choice = ''
    while choice != '4':
        print(
            'Варианты действия:',
            '1. Добавление контакта',
            '2. Вывод данных на экран',
            '3. Поиск контакта',
            '4. Копирование контакта',
            '5. Выход',
            sep='\n'
           )

        print()
        choice = input('Выберите действие: ')
        print()
        while choice not in ['1', '2', '3', '4', '5']:
            print('Не корректный ввод данных!')
            choice = input('Выберите действие: ')
        # print()

        match choice:
            case '1':
                data_input()
            case '2':
                print_data()
            case '3':
                search_contact()
            case '4':
                copy_contact()
            case '5':
                print('Всего доброго!')


def copy_contact():
    contacts = read_file()
    contacts_list = contacts.strip().split('\n\n')
    num_contact = int(input('Введите номер контакта, который желаете скопировать: ')) - 1
    file_name = input('Введите имя файла, куда хотите скопировать контакт: ')

    with open(f'{file_name}.txt', 'a', encoding='utf-8') as file:
        file.write(f'{contacts_list[num_contact]}\n\n')


if __name__ == '__main__':

    interface()


