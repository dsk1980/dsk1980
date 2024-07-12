immutable_var = 1, 2, 3, 'a', 'b', 'c', True, [1, 2, 3]
# immutable_var[1] = 5 TypeError: объект 'tuple' не поддерживает назначение элементов.
# Кортеж хранит ссылку на список, а не сам список.
print(immutable_var)

mutable_list = [1, 2, 3, 'a', 'b', 'c', True]
mutable_list[4]='Modified'
print(mutable_list)
