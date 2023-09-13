# Планеты вращаются вокруг звезд по эллиптическим орбитам.
# Назовем самой далекой планетой ту, орбита которой имеет
# самую большую площадь. Напишите функцию
# find_farthest_orbit(list_of_orbits), которая среди списка орбит
# планет найдет ту, по которой вращается самая далекая
# планета. Круговые орбиты не учитывайте: вы знаете, что у
# вашей звезды таких планет нет, зато искусственные спутники
# были были запущены на круговые орбиты. Результатом
# функции должен быть кортеж, содержащий длины полуосей
# эллипса орбиты самой далекой планеты. Каждая орбита
# представляет из себя кортеж из пары чисел - полуосей ее
# эллипса. Площадь эллипса вычисляется по формуле S = pi*a*b,
# где a и b - длины полуосей эллипса. При решении задачи
# используйте списочные выражения. Подсказка: проще всего
# будет найти эллипс в два шага: сначала вычислить самую
# большую площадь эллипса, а затем найти и сам эллипс,
# имеющий такую площадь. Гарантируется, что самая далекая
# планета ровно одна
# Ввод:
# orbits = [(1, 3), (2.5, 10), (7, 2), (6, 6), (4, 3)]
# print(*find_farthest_orbit(orbits))
# Вывод:
# 2.5 10

# def find_farthest_orbit(list_of_orbits):
#     new_lst = []
#     max_orb = 0
#     for i in range(len(list_of_orbits)):
#         a,b = list_of_orbits[i]
#         new_lst.append(a*b)
#         if a != b:
#             s = a*b
#             if s > max_orb:
#                 max_orb = s
#     return list_of_orbits[new_lst.index(max_orb)]
                    
# def find_farthest_orbit(list_of_orbits):
#     filter_orbit = list(filter(lambda x: x[0] != x[1], list_of_orbits))
#     square = list(map(lambda x: x[0]*x[1], filter_orbit))
#     orbit_dict = dict(zip(square,filter_orbit))
#     max_orbit = max(orbit_dict.keys())
#     return orbit_dict.get(max_orbit)



orbits = [(1, 3), (2.5, 10), (7, 2), (6, 6), (4, 3)]
# print(find_farthest_orbit(orbits))
print(max(orbits, key= lambda x  : x[0] * x[1]*(x[0]!=x[1])))