# Узнайте у пользователя число n. Найдите сумму чисел n + nn + nnn.
# Например, пользователь ввёл число 3. Считаем 3 + 33 + 333 = 369.

number = input('Введите число\n')

if number.isdigit():
    number1 = number + number
    number2 = number + number + number

    print('{}'.format(int(number) + int(number1) + int(number2)))
else:
    print('Вы ввесли не число')

