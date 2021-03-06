# Создать программный файл в текстовом формате, записать в него построчно данные,
# вводимые пользователем. Об окончании ввода данных будет свидетельствовать пустая строка.
with open("lesson5.txt", "w") as lesson:
    stop_symbol = ""
    while True:
        result = input("write something")
        if result == stop_symbol:
            break
        else:
            lesson.write(result + "\n")
            continue


