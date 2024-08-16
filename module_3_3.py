def print_params(a=1, b='string1', c=True):
    print(a, b, c)


print_params()
print_params(5)
print_params(b=9)  # ругается из-за смены типа данных
print_params(b='9')
print_params(c=[3, 5, 7])  # ругается из-за смены типа данных

values_list = (9, False, 'String2')
print(values_list)
print_params(*values_list)
values_dict = {'a': 1, 'b': 'string', 'c': True}
print(values_dict)
print_params(**values_dict)

values_list_2 = (10, 'String3')
print_params(*values_list_2, 42)  # Работает, новый элемент добавляется.
