# Дан список чисел. Определите, сколько в нем
# встречается различных чисел.
# Input: [1, 1, 2, 0, -1, 3, 4, 4, 1, 6, 5, 0]
# Output: 6

row = [1, 1, 2, 0, -1, 3, 4, 4,1, 6, 5, 0]
# print(len(set(row)))
row2 = []
i = 1
temp = row[0]
for i in row:
    if i not in row2:
        row2.append(i)
print(row2)
print(len(row2))



        