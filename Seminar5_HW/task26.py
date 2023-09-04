# Напишите программу, которая на вход принимает
# два числа A и B, и возводит число А в целую степень B с
# помощью рекурсии.


def Pow(a,b):
    if b == 0:
        return 1
    return Pow(a,b-1) * a
    

firstNum = int(input("Введите число: "))
secondNum = int(input("Введите степень: "))
print(f"result = {Pow(firstNum,secondNum)}")

