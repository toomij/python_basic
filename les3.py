def my_pow(a: float) -> float:
    result = a ** 2
    return result


# функция генератор
def my_map(func, temp):
    for itm in temp:
        print("START")
        yield func(itm)
        print("YELD 1 DONE")
        yield func(itm) + 15
        print("CYCLE DONE")
    return None


def my_func(a):
    a += 1

    def help(b):
        return a + b

    return help


def my_except():
    num = 22
    while True:
        try:
            a = int(input('Введите число '))
            result = num / a
            break
        except ValueError as error:
            print(error)
            print('Тут код обработки ошибки')
            continue
        except ZeroDivisionError:
            result = 0
            break
        except Exception:
            print('HELLO')
        finally:
            print('ВЫполняется всегда')

    return result


def my_func2(temp: list) -> float:
    temp.append(2345)
    print(temp)
    return sum(temp)


def func3(a, b, c, d):
    return sum((a, b, c, d))


a = [1, 2, 3, 4]
print(a)

m_d = {
    'a': 2,
    'b': 3,
    'c': 4,
    'd': 5,
}


def my_max(*args, **kwargs):
    print('KWARGS', type(kwargs))
    print(kwargs)
    print(type(args))
    result = float('inf') * -1
    for itm in args:
        if result < itm:
            result = itm
    return result


# result = my_max(1, 2, 3, 4, 5, 6, 7, key=my_pow)
#
# print(result)

a, b, c, *d = input('HELLO').split(' ')
print(a, b, c, d)

# анонимная функция
lambda x: x ** 2

# тернарная операции