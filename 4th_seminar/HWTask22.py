# Даны два неупорядоченных набора целых чисел (может быть, с повторениями). Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах.
# Пользователь вводит 2 числа. n — кол-во элементов первого множества. m — кол-во элементов второго множества. Затем пользователь вводит сами элементы множеств.

n = int(input("Введите количество элементов первого множества: "))
m = int(input("Введите количество элементов второго множества: "))
first = ""
second = ""
result = []
for i in range(n):
    first += input(f"{i+1}-ое число: ")
print(first)

for i in range(m):
    second += input(f"{i+1}-ое число: ")
print(second)

first.split()
second.split()

if n >= m:
    for i in range(len(first)):
        if (first[i] in second):
            result.append(first[i])
else:
    for i in range(len(second)):
        if (second[i] in first):
            result.append(second[i])
            
print(result.sort())
