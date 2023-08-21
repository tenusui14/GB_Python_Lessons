# ввести два числа и определить какое из них больше
first = int(input("Первое число = "))
second = int(input("Второе число = "))
print()

if first > second:
    print(f"{first} - Первое больше")
elif second > first:
    print(f"{second} - Второе больше")
else:
    print("Числа равны")