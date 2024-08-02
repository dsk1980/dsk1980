name = input('Введите ваше имя: ')
print('Здравствуйте,', name)
number1 = int(input('Введите первое число: '))
number2 = int(input('Введите второе число: '))
number3 = int(input('Введите третье число: '))
if number1 == number2 and number2 == number3 and number3 == number1:
    print('3')
elif number1 == number2 != number3 or number2 == number3 != number1 or number3 == number1 != number2:
    print('2')
else:
    print('0')
