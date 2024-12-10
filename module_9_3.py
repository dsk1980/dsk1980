# Домашнее задание по теме "Генераторные сборки".

first = ['Strings', 'Student', 'Computers']
second = ['Строка', 'Урбан', 'Компьютер']

'''1.В переменную first_result запишите генераторную сборку, которая
высчитывает разницу длин строк из списков first и second, если их длины
не равны. Для перебора строк попарно из двух списков используйте функцию zip.'''

first_result = (len(f)-len(s) for f, s in zip(first, second) if len(f) != len(s))

'''В переменную second_result запишите генераторную сборку,
которая содержит результаты сравнения длин строк в одинаковых позициях
из списков first и second. Составьте эту сборку НЕ используя функцию zip.
Используйте функции range и len.'''

second_result = (len(first[f]) == len(second[f]) for f in range(len(first)))

# Результат:
print(list(first_result))
print(list(second_result))
