# Рекурсия

def get_multiplied_digits(number):
    str_number = str(number)

    first = int(str_number[0])
    if len(str_number) > 1:
        if int(str_number[1:]) == 0:
            return first
        elif int(str_number[1:]) != 0:
            return (first * get_multiplied_digits(int(str_number[1:])))
    else:
        return first


print(get_multiplied_digits(402030))
print(get_multiplied_digits(5754680674))
print(get_multiplied_digits(1010))
