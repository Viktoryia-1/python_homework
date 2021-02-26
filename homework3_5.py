# Программа запрашивает у пользователя строку чисел, разделённых пробелом. При нажатии Enter
# должна выводиться сумма чисел. Пользователь может продолжить ввод чисел, разделённых пробелом
# и снова нажать Enter. Сумма вновь введённых чисел будет добавляться к уже подсчитанной сумме.
# Но если вместо числа вводится специальный символ, выполнение программы завершается.
# Если специальный символ введён после нескольких чисел, то вначале нужно добавить сумму этих чисел
# к полученной ранее сумме и после этого завершить программу.


#print(your_numbers)
def numbers(*args):
    new_list = [int(el) for el in your_numbers]
    #print(new_list)
    sum_new_list = sum(new_list)
    #print(sum_new_list)
    return sum_new_list
#
# your_numbers = input("введите строку числе через пробел").split()
# a = numbers(your_numbers)
# print(a)


z = 0
while True:
    your_numbers = input("введите строку числе через пробел").split()
    if your_numbers[-1] != "stop":
        z = z + numbers(your_numbers)
        print(z)
        continue
    elif your_numbers[-1] == "stop":
        your_numbers = your_numbers[:-1]
        a = numbers(your_numbers)
        z = a + z
        print(z)
        break







#total_sum = sum(your_numbers_list)