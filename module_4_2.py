def test_function():
    def inner_function():
        print('Я в области видимости функции test_function')
    inner_function()
#inner_function() # Ошибка NameError: имя 'inner_function' не определено. Вы имели в виду 'test_function'?