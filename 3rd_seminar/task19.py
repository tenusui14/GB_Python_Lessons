# Дана последовательность из N целых чисел и число
# K. Необходимо сдвинуть всю последовательность
# (сдвиг - циклический) на K элементов вправо, K –
# положительное число.
# Input: [1, 2, 3, 4, 5] k = 3
# Output: [4, 5, 1, 2, 3]
# Примечание: Пользователь может вводить значения
# списка или список задан изначально.

row = [1, 2, 3, 4, 5]
k = 3
print(row[k:]+ row[:k])

# array_in = [1, 2, 3, 4, 5]
# k = 3
# if k < len(array_in):
#    array_out = array_in[k:] + array_in[:k]
#    print(array_out)










