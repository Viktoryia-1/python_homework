# Сформировать (не программно) текстовый файл. В нём каждая строка должна описывать
# учебный предмет и наличие лекционных, практических и лабораторных занятий по предмету.
# Сюда должно входить и количество занятий. Необязательно,
# чтобы для каждого предмета были все типы занятий.
# Сформировать словарь, содержащий название предмета и общее количество занятий по нему.
# Вывести его на экран.
# Примеры строк файла:                    Информатика:   100(л)   50(пр)   20(лаб).
#                                         Физика:   30(л)   —   10(лаб)
#                                         Физкультура:   —   30(пр)   —
# Пример словаря: {“Информатика”: 170, “Физика”: 40, “Физкультура”: 30}

with open("lesson5_6.txt", "r", encoding="utf-8") as task_6:

    key_list = []
    third_list = []
    for line in task_6:
        line = line.split()
        a = line[0]
        key_list.append(a)
        b = line[1:]
        second_list = []
        third_list.append(second_list)
        for el in b:
            el = [i for i in el if i.isdigit()]
            el = "".join(el)
            second_list.append(el)
            for i in second_list:
                if i == "":
                    second_list.remove(i)
    fo_list = []
    for el in third_list:
        list_list = [int(i) for i in el]
        fo_list.append(list_list)

    finish_values = [sum(el) for el in fo_list]

    final = dict(zip(key_list, finish_values))
    print(final)


























    

