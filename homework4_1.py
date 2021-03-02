from sys import argv


name, ours, rate, award = argv


print(f'это имя {name}')
print(f'это часы {ours}')
print(f'это ставка {rate}')
print(f'это премия {award}')

salary = float(ours) * float(rate) + float(award)
print(round(salary))





