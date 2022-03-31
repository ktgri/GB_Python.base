# Реализовать функцию int_func(), принимающую слова из маленьких латинских букв и возвращающую их же,
# но с прописной первой буквой. Например, print(int_func(‘text’)) -> Text.

int_func = lambda string: string[0].upper() + string[1:].lower()

print(int_func("TesTIng test testik ttt"))
