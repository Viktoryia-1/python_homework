# Создать (программно) текстовый файл, записать в него программно набор чисел,
# разделённых пробелами. Программа должна подсчитывать сумму чисел в файле и выводить её на экран.

with open("lesson5_5.txt", "w", encoding="utf-8") as task_5:
    numbers = input("Введите числа через пробел: ")
    task_5.write(numbers)


with open("lesson5_5.txt", "r", encoding="utf-8") as task_5:
    numbers = task_5.read()
    numbers = numbers.split()
    list_numbers = [int(i) for i in numbers]
    print(list_numbers)
    result = sum(list_numbers)
    print(result)
