# Дано натуральное число A > 1. Определите, каким по счету числом Фибоначчи оно является, то есть выведите такое число n, что φ(n)=A. 
# Если А не является числом Фибоначчи, выведите число -1.
# Input: 5 Output: 6

n = int(input("Введите число: "))
fibonnachi = 0
zero_fibb = 0
first_fibb = 1
i = 0
while fibonnachi <= n:
    zero_fibb = fibonnachi
    fibonnachi = first_fibb + fibonnachi
    first_fibb = zero_fibb
    i += 1
    if n == fibonnachi:
        print(i)
        break
if n == 0:
      print(0)
elif n < 0 or n != fibonnachi:
     print(-1)
