with open("lesson5_3.txt", "r", encoding="utf-8") as task_3:
    count_sum = 0
    count_people = 0
    less_list = ""

    for el in task_3:
        el = el.split()
        salary = int(el[1])
        count_sum += salary
        count_people += 1
        if salary < 20000:
            less_list += "\n" + (el[0])

    result = count_sum / count_people
    print(f"Сумма зарплаты всех сотрудников равна {count_sum}")
    print(f"Средняя зарплата сотрудника равна {result}")
    print(f"Наименее оплачиваемые сотрудники (менее 20000): {less_list}")










