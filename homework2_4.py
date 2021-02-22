st = input("введите значения через пробел").split()
for ind, el in enumerate(st, 1):
    print(ind, el) if len(el) <= 10 else print(ind, (el[:10]))