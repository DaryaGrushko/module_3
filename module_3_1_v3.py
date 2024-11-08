# Домашняя работа по уроку "Пространство имён"
calls = 0

def count_calls():
    global calls
    calls += 1

def string_info(string_):
    count_calls()
    return (len(string_), string_.upper(), string_.lower())

def is_contains(string_, list_to_search):
    str1 = string_.lower()
    new_list = [x.lower() for x in list_to_search]
    count_calls()
    if str1 in new_list:
        return True
    else:
        return False

print(string_info('Capybara'))
print(string_info('Armageddon'))

print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN']))
print(is_contains('cycle', ['recycling', 'cyclic']))

print  (calls)
