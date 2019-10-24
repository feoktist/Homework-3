numbers = []
item = 1
items_number = (input("Введите количество элементов: "))
items_number = int(items_number)
while item <= items_number:
    element = int((input("Введите элемент: ")))
    numbers.append(element)
    item = item + 1

numbers.sort()
print(numbers)