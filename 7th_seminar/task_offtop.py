# Вводится список целых чисел в одну строчку через пробел. Необходимо оставить в нем только двузначные числа.
# Реализовать программу с использованием функции filter. 
# Результат отобразить на экране в виде последовательности оставшихся чисел в одну строчку через пробел.


# пример  - 8 11 0 -23 140 1  вывод - 11-23

lst = list(map(int,input("Введите числа через пробел ").split()))
print(lst)

filtr = list(filter(lambda x: 9 < abs(x) < 100, lst))
print(filtr, end = '')


