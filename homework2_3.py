seasons = ["winter", "spring", "summer", "autumn"]
seasons_d = {1:"winter", 2:"spring", 3:"summer", 4:"autumn"}
month = int(input("введите число от 1 до 12"))
if month == 12 or month == 1 or month == 2:
    print(seasons[0])
    print(seasons_d.get(1))
if month == 3 or month == 4 or month == 5:
    print(seasons[1])
    print(seasons_d.get(2))
if month == 6 or month == 7 or month == 8:
    print(seasons[2])
    print(seasons_d.get(3))
if month == 9 or month == 10 or month == 11:
    print(seasons[3])
    print(seasons_d.get(4))
if month < 0 or month > 12:
    print("error")