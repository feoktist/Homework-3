print('Введите элементы 1 списка через запятую: ')
print('(Нажмите Enter для завершения ввода)')
a = [int(x) for x in input().split(',')]
aa = set(a)

print('Введите элементы 2 списка через запятую: ')
print('(Нажмите Enter для завершения ввода)')
b = [int(x) for x in input().split(',')]
bb = set(b)

# Удалить из первого списка элементы присутствующие во 2-ом и вывести результат на экран
result = aa - bb
print(result)