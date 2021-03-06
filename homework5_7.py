# Создать вручную и заполнить несколькими строками текстовый файл,
# в котором каждая строка будет содержать данные о фирме:
# название, форма собственности, выручка, издержки.
# Пример строки файла: firm_1   ООО   10000   5000.
# Необходимо построчно прочитать файл, вычислить прибыль каждой компании,
# а также среднюю прибыль. Если фирма получила убытки, в расчёт средней прибыли её не включать.
# Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями,
# а также словарь со средней прибылью. Если фирма получила убытки,
# также добавить её в словарь (со значением убытков).
# Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].
# Итоговый список сохранить в виде json-объекта в соответствующий файл.
# Пример json-объекта:
# [{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]
# Подсказка: использовать менеджер контекста.
import json
with open("lesson5_7.txt", "r", encoding="utf-8") as task_7:
    result_list = []
    firm_list = []
    for i in task_7:
        line = i.split()
        profit = int(line[2])
        loss = int(line[3])
        result = profit - loss
        result_list.append(result)
        firm_list.append(line[0])

    firm_dict = dict(zip(firm_list, result_list))

    plus_list = [i for i in result_list if i > 0]

    sum_profit = sum(plus_list) / len(result_list)

    average_dict = {"average_profit": sum_profit}

    final_list = [firm_dict, average_dict]
    print(final_list)

with open("lesson5_7.json", "w", encoding="utf8") as task7_1:
    json.dump(final_list, task7_1)
