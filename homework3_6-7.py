# Реализовать функцию int_func(), принимающую слова из маленьких латинских букв и возвращающую их же,
# но с прописной первой буквой. Например, print(int_func(‘text’)) -> Text.

def my_str(one_str):
    low_string = str(one_str)
    low_string = low_string.title()
    return low_string


title_string = my_str("hello there")
print(title_string)


# Продолжить работу над заданием. В программу должна попадать строка из слов, разделённых пробелом.
# Каждое слово состоит из латинских букв в нижнем регистре. Нужно сделать вывод исходной строки,
# но каждое слово должно начинаться с заглавной буквы. Используйте написанную ранее функцию int_func().


your_string = input("Введите слова строчными буквами через пробел: ")
your_string = my_str(your_string)
print(your_string)