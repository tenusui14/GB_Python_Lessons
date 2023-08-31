# Задача №21. Решение в группах
# Напишите программу для печати всех уникальных
# значений в словаре.
# Input: [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"},
# {"VI": "S005"}, {"VII": " S005 "}, {" V ":" S009 "}, {" VIII
# ":" S007 "}]
# Output: {'S005', 'S002', 'S007', 'S001', 'S009'}
# Примечание: Список словарей задан изначально.
# Пользователь его не вводит

# dict = {"V": "S001", "V": "S002", "VI": "S001",
#         "VI": "S005", "VII": "S005", "V": "S009", "VIII": "S007"}
# unique = set(dict.values())
# print(unique)

row = [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII": "S005"}, {"V": "S009"}, {"VIII": "S007"}]

row1 = set()
for i in row:
    for j in i.values():
        row1.add(j)
print(row1, end= ",")
