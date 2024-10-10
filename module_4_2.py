def test_function():
    print(test_function())
    def inner_function():
        print(inner_function())

# print(inner_function()) # Ошибка NameError: имя 'inner_function' не определено.
