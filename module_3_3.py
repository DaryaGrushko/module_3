#Домашнее задание по уроку "Распаковка позиционных параметров".
def  print_params(a = 1, b = 'строка', c = True):
    print(a,b,c)

print_params()
print_params(b = 25)
print_params(c = [1,2,3])
print_params(a = 1,b = 2)
print_params(a = 1,b = 2, c = 3)

values_list = ['Name', 12345, False]
print_params(*values_list)
values_dict = {'a' : 1111, 'b': 'NameName', 'c' : True}
print_params(**values_dict)

values_list_2 = ['Hi', 'QQQQuuu']
print_params(*values_list_2, 42)

