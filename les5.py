# try:
#     file = open('input.txt', 'r', encoding='UTF-8')
# except IOError:
#     print('ОШИБКА')
# finally:
#     file.close()

# for line in file:
#     print(line, end='')
#
# print(file.read(8))
# print(file.read(8))

# with open('output.txt', 'wb') as out_file:
#     content = bytes('HELLO MY DEAR FRENDS. ЭТО БАЙТОВАЯ СТРОКА', encoding='UTF-8')
#     print(content)
#     out_file.write(content)

# JSON
# import json
#
# data = {
#     'key1': [1, 2, 3],
#     'key2': True,
#     'key3': None,
#     'key4': 'HELLO МИР"',
#     'key5': (1, 2, 3, 4),
# }
#
# new_data = [data, data]
# j_data = json.dumps(new_data, ensure_ascii=False)
#
# print(j_data)
#
# with open('j_data.json', 'r') as j_file:
#     print(json.load(j_file))
#
# # кортеж обратно не получим
# print(json.loads(j_data))
#

import os

# print(os.listdir('.'))
# print(os.path.isdir('env'))
dir_path_root = os.path.dirname(__file__)
#
file_name = 'output.txt'
# print(os.path.dirname(__file__))
# print(__file__)
#
full_path = os.path.join(dir_path_root, file_name)
# print(full_path)

# os.rename(full_path, 'new_name.txt')


# print(os.system('ls'))
# print(os.path.exists(full_path))
#
# with open(full_path, 'r') as in_file, open('new_copy.txt', 'w') as cop_file:
#     cop_file.write(in_file.read())
#
# import shutil
#
# shutil.copy(full_path, 'new_cop.txt')

# import sys


# print(sys.path)

import requests

response = requests.get('https://api.github.com/users/gefmar')

with open('gb.html', 'w', encoding='UTF-8') as file:
    file.write(response.text)

data = response.json()
print(data['login'])

