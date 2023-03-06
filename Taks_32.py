# Задача 32: Определить индексы элементов массива (списка), значения которых принадлежат заданному диапазону 
# (т.е. не меньше заданного минимума и не больше заданного максимума)

m = int (input('Введите количество элементов: '))
list_1 = [0] * m
for i in range (m):
    list_1[i] = int (input('Введите элемент:  '))
    list_1.append
print(list_1)
min_elem = int (input('Введите минимальный элемент: '))
max_elem = int (input('Введите максимальный элемент: '))
for element in list_1:
    if min_elem <= element <= max_elem:
        print("Индекс элемента {} в списке = {}".format(element, list_1.index(element)))
