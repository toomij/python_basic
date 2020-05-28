"""6. Реализовать функцию int_func(), принимающую слово из маленьких латинских букв и возвращающую его же, но с прописной первой буквой. Например, print(int_func(‘text’)) -> Text."""

def int_func(text):
  var_list = []
  output_list = []
  var_list = text.split(' ')
  for wd in var_list:
    output_list.append(wd.capitalize())
  return ' '.join(map(str, output_list))


print(int_func('test test test'))