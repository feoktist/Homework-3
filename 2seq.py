print('Введите элементы списка через запятую: ')
print('(Нажмите Enter для завершения ввода)')
a = [int(x) for x in input().split(',')]

b = list()
for i in a:
   if a.count(i) == 1:
       b.append(i)
print(b)