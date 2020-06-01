# Пользователь вводит целое положительное число.
# Найдите самую большую цифру в числе.
# Для решения используйте цикл while и арифметические операции.

number_str = input('Введите положительное целое число\n')

if number_str.isdigit():
    number = int(number_str)
    temp = number // 10
    nmax = number % 10

    nmin = 0
    while temp != 0:

        nmin = temp % 10

        if nmax <= nmin:
            nmax = nmin
        temp //= 10
    print(nmax)
else:
    print('Вы ввели не число')


# number = []
#
# for i in range(len(number_str)):
#     number.append(number_str[i])
#
# max_num = number[0]
#
# i = 0                       # индекс, счётчик
# nmin = i                    # номер минимального элемента
# min = number[nmin]          # собственно минимальный элемент
# nmax = i                    # номер максимального элемента
# max = number[nmax]          # собственно максимальный элемент
# while (i < len(number)):
#     if (number[i] < min):
#         nmin = i
#         min = number[nmin]
#     if (number[i] > max):
#         nmax = i
#         max = number[nmax]
#     i += 1
#
# print("max = a[", nmax, "] = ", max)
