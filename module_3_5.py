# Рекурсия

def get_multiplied_digits(number):
    str_number = str(number)
    first = int(str_number[0])
    print('number =', number, 'first = ', first)
    if len(str_number) > 1:
        return (first * get_multiplied_digits(int(str_number[1:])))
    else:
        return first


print(get_multiplied_digits(40203))
print(get_multiplied_digits(5754680674))
print(get_multiplied_digits(1))
