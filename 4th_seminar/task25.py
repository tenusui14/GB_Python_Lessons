# Напишите программу, которая принимает на вход
# строку, и отслеживает, сколько раз каждый символ
# уже встречался. Количество повторов добавляется к
# символам с помощью постфикса формата _n.
# Input: a a a b c a a d c d d
# Output: a a_1 a_2 b c a_3 a_4 d c_1 d_1 d_2
# Для решения данной задачи используйте функцию .split()

text = input("Введите строку символов через пробел: ").split()
dict = {}
resultStr = ""

for i in range(len(text)):
    if text[i] not in dict.keys():
        dict[text[i]] = 1
        resultStr += f"{text[i]} "
    else:
        resultStr += f"{text[i]}_{dict[text[i]]} "
        dict[text[i]] += 1
print(resultStr)