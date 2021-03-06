# Создать (не программно) текстовый файл со следующим содержимым:
# One — 1
# Two — 2
# Three — 3
# Four — 4
# Напишите программу, открывающую файл на чтение и считывающую построчно данные.
# При этом английские числительные должны заменяться на русские. Новый блок строк
# должен записываться в новый текстовый файл.
from translate import Translator
with open("lesson5_4.txt", "r", encoding="utf-8") as task_4:
    with open("lesson5_second_4.txt", "w", encoding="utf8") as final:
        for line in task_4:
            line = line.split()
            translator = Translator(to_lang="Russian")
            el = translator.translate(line[0])
            line.insert(1, el)
            line.pop(0)
            line = " ".join(line)
            final.write(line + "\n")
















