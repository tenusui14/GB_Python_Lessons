# Заполните массив элементами арифметической
# прогрессии. Её первый элемент, разность и количество
# элементов нужно ввести с клавиатуры. Формула для
# получения n-го члена прогрессии: an = a1 + (n-1) * d.
# Каждое число вводится с новой строки.

# Ввод: 7 2 5
# Вывод: 7 9 11 13 15



# data = (input("Введите первый элемент, разность и кол-во элементов через пробел: "))
# data = list(map(int, data.split()))

firstElement = int(input("Введите первый элемент: "))
diff = int(input("Введите разность: "))
quantity = int(input("Введите количество элементов: "))
res = []
for i in range(1,quantity+1):
    res.append(firstElement + ((i-1)*diff))
print(res)

