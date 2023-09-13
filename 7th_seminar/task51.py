# Напишите функцию same_by(characteristic, objects), которая
# проверяет, все ли объекты имеют одинаковое значение
# некоторой характеристики, и возвращают True, если это так.
# Если значение характеристики для разных объектов
# отличается - то False. Для пустого набора объектов, функция
# должна возвращать True. Аргумент characteristic - это
# функция, которая принимает объект и вычисляет его
# характеристику.
# Ввод:
# values = [0, 2, 10, 6] 
# if same_by(lambda x: x % 2, values):
# print(‘same’)
# else:
# print(‘different’)

# Вывод: same


def same_by(characteristics, objects):
    filtered_lst = list(filter(characteristics,objects))

    if filtered_lst == objects:
        return True
    else: return False

def characteristic(x):
    return x <= 0


values = [-2,-4,-6, -1]
print(same_by(characteristic,values))
