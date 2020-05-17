# Пользователь вводит время в секундах.
# Переведите время в часы, минуты и секунды и выведите в формате чч:мм:сс.
# Используйте форматирование строк.


seconds_in_hour = 3600
seconds_in_minute = 60

seconds = input("Enter a number of seconds: ")


if seconds.isdigit():
    seconds = int(seconds)
    hours = seconds // seconds_in_hour
    seconds = seconds - (hours * seconds_in_hour)
    minutes = seconds // seconds_in_minute
    seconds = seconds - (minutes * seconds_in_minute)
    print("{0:.0f}:{1:.0f}:{2:.0f}".format(hours, minutes, seconds))
else:
    print('Не было введено число')



