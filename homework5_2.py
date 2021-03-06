with open("lesson5_2.txt", "r") as lesson_2:
    line_count = 0
    symbols_count = 0
    words_count = 0
    for line in lesson_2:
        print(line, end="")
        line_count += 1

    lesson_2.seek(0)
    for line in lesson_2:
        count = len(line)
        symbols_count += count
        for el in line:
            if el == "\n" or el == " ":
                symbols_count -= 1

    lesson_2.seek(0)
    for line in lesson_2:
        sep_list = line.split()
        line_worlds = len(sep_list)
        words_count += line_worlds


print("\n", f"Количество строк в файле равно {line_count}")
print("\n", f"Количество символов в файле равно {symbols_count}")
print("\n", f"Количество слов в файле равно {words_count}")