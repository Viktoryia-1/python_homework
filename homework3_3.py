# Реализовать функцию my_func(), которая принимает три позиционных аргумента
# и возвращает сумму наибольших двух аргументов.


def my_func(num_1, num_2, num_3):
    my_list = []
    my_list.append(num_1)
    my_list.append(num_2)
    my_list.append(num_3)
    first_num = max(my_list)
    my_list.remove(first_num)
    second_num = max(my_list)
    summ = first_num + second_num
    return summ


a = my_func(1, 3, 5,)
print(a)

# Хотелось создать список с помощью цикла, но получилось только с неопределенным числом аргументов


def my_func(*args):
    my_list = []
    n = len(args)
    for i in range(n):
        my_list.append(args[i])
    first_num = max(my_list)
    my_list.remove(first_num)
    second_num = max(my_list)
    summ = first_num + second_num
    return summ


a = my_func(1, 3, 5, 8, 9)
print(a)