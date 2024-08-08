name = input('Введите ваше имя: ')
print('Здравствуйте,', name)
print('Домашняя работа по уроку "Функции в Python.Функция с параметром" - Задача "Матрица воплоти"')
def get_matrix(n, m, value):
    matrix = []
    for i in range(n):
        matrix.append([])
        for j in range(m):
            matrix[i].append(value)
        print(matrix)
    return matrix
n = int(input('Введите количество строк матрицы: '))
m = int(input('Введите количество столбцов матрицы: '))
value = input(f'Задайте значения матрицы : ')
print('' * m)
matrix = get_matrix(n, m, value)