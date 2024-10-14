# Домашняя работа по уроку "Пространство имён"
calls = 0

def count_calls():
    global calls
    calls += 1
    print ('Счетчик вызова функций = ', calls)

def string_info(string_):
    print('----------- Вызов функции', calls + 1, 'раз ---------------')
    print('Строка - "', string_, '')
    print('Длина строки - ', len(string_), '\nСтрока в верхнем регистре -', string_.upper(),
          '\nСтрока в нижнем регистре -', string_.lower())
    count_calls()

def is_contains(string_, list_to_search):
    print('----------- Вызов функции', calls + 1, 'раз ---------------')
    # print ('Строка string_ = "', string_, '" , список list_to_search = "', list_to_search, '"' )
    str1 = string_.lower()
    new_list = [x.lower() for x in list_to_search]
    # print('str1_ = ', str1, 'new_list = ', new_list)
    if str1 in new_list:
        print('True - строка "', string_, '" содержится в  списке ', list_to_search, '(без учета регистра)')
    else:
        print('True - строка "', string_, '" НЕ содержится в  списке ', list_to_search, '(без учета регистра)')
    count_calls()

string_ = input('Введите строку:')
string_info(string_)

string_info('Capybara')
string_info('Armageddon')
string_info('Hello, Roman!')

is_contains('Urban', ['ban', 'BaNaN', 'urBAN'])
is_contains('cycle', ['recycling', 'cyclic'])
is_contains('Sasha', ['Dasha', 'SAsha', 'Igor'])
is_contains('123', ['5745754745', '123', '677'])
