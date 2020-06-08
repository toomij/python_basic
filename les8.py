import requests

class Product:
    name = 'NO NAME'

    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)

    def __str__(self):
        return self.name


class Catalog:
    __api_url = 'https://5ka.ru/api/v2/special_offers/'
    __headers = {
        'User-agent' : 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_4) '
                        'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36'

    }

    def __init__(self):
        self.products = []

    def parse(self):
        url = self.__api_url
        while url:
            response = requests.get(url, headers=self.__headers)
            data = response.json()
            url = data.get('next')
            self.products.extend([Product(**itm) for itm in daata['results']])


class MyCls:
    a = 22
    b = 33

    def __init__(self, data: str, a, b):
        self.data = data
        self.a = a
        self.b = b

    @staticmethod
    def some(a, b):
        return a + b

    @classmethod
    def some_cls(cls):
        return cls.a + cls.b


if __name__ == '__main__':
    # a = MyCls('some name', 2, 5)
    # print(MyCls.some_cls())
    # print(a.a + a.b)
    # print(MyCls.__name__)
    # print(a.__dict__)
    # print(a.__module__)
    catalog = Catalog()
    catalog.parse()
    print(1)
