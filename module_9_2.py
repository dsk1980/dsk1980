# Домашнее задание по теме "Списковые, словарные сборки".

first_strings = ['Elon', 'Musk', 'Programmer', 'Monitors', 'Variable']
second_strings = ['Task', 'Git', 'Comprehension', 'Java', 'Computer', 'Assembler']

'''1.В переменную first_result запишите список созданный при помощи сборки
состоящий из длин строк списка first_strings, при условии,
что длина строк не менее 5 символов.'''

first_result = [len(s_1) for s_1 in first_strings if len(s_1) >= 5]

'''2.В переменную second_result запишите список созданный при помощи сборки
состоящий из пар слов(кортежей) одинаковой длины. Каждое слово из списка
first_strings должно сравниваться с каждым из second_strings. (два цикла)'''

second_result = [(s_1, s_2) for s_1 in first_strings for s_2 in second_strings if len(s_1) == len(s_2) ]

'''3.В переменную third_result запишите словарь созданный при помощи
сборки, где парой ключ-значение будет строка-длина строки. Значения строк
будут перебираться из объединённых вместе списков first_strings и
second_strings. Условие записи пары в словарь - чётная длина строки.'''

third_result = {s: len(s) for s in first_strings + second_strings if len(s) % 2 == 0}

# Результат:
print(first_result)
print(second_result)
print(third_result)
