# Определить индексы элементов массива (списка),
# значения которых принадлежат заданному диапазону (т.е. не
# меньше заданного минимума и не больше заданного
# максимума)

# заданный диапазон: х1 = 5 х2 = 15 (нужно вывести индексы чисел, попадающих в этот диапазон)

# Ввод: [-5, 9, 0, 3, -1, -2, 1,
# 4, -2, 10, 2, 0, -9, 8, 10, -9,
# 0, -5, -5, 7]
# Вывод: [1, 9, 13, 14, 19]

lst = [-5, 9, 0, 3, -1, -2, 1, 4, -2, 10, 2, 0, -9,
       8, 10, -9, 0, -5, -5, 7, 20, 35, 76, -2, 14, -11, 13, 34, 63, -22]
res = []
start = int(input("Введите минимальное значение: "))
fin = int(input("Введите максимальное значение: "))

for i in range(len(lst)):
    if lst[i] >= start and lst[i] <= fin:
        res.append(i)
print(res)