# Задача 10: На столе лежат n монеток. Некоторые из них лежат вверх решкой, а некоторые – гербом. 
# Определите минимальное число монеток, которые нужно перевернуть, чтобы все монетки были повернуты вверх одной и той же стороной. 
# Выведите минимальное количество монет, которые нужно перевернуть
# 5 -> 1 0 1 1 0
# 2

text = input("Последовательность положения монеток(0 или 1): ")
count_0 = 0
count_1 = 0
res = 0
for i in range(len(text)):
    if(text[i] == "1"): count_1 += 1
    if(text[i] == "0"): count_0 += 1
if(count_1 > count_0): res = count_0
else: res = count_1
print(f"Минимальное колво монет, которые нужно перевернуть: {res}")


