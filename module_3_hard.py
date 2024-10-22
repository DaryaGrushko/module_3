# Дополнительное практическое задание по модулю: "Подробнее о функциях."

data_structure = [
    [1, 2, 3],
    {'a': 4, 'b': 5},
    (6, {'cube': 7, 'drum': 8}),
    "Hello",
    ((), [{(2, 'Urban', ('Urban2', 35))}])
]
count = 0

def calculate_structure_sum(*params):
    global count
    for i in params:  # убираем первый внешний кортеж
        for j in i:  # перебираем элементы списка
            print('Функция запущена с параметром  j = ', j)
            if isinstance(j, str):
                count += int(len(j))
                print(j, ' - Тип строка,', '+ ', int(len(j)), ', count', count)
            elif isinstance(j, int):
                count += j
                print(j, ' - тип число, ', '+  ', j, ', count', count)
            elif isinstance(j, dict):
                for k in j:
                    calculate_structure_sum({k, j[k]})
            else:
                calculate_structure_sum(j)
            print()
    return count

result = calculate_structure_sum(data_structure)
print('Результат суммы =', result)
