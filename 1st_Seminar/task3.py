# В некоторой школе решили набрать три новых математических класса и оборудовать кабинеты для них новыми партами. 
# За каждой партой может сидеть два учащихся. Известно количество учащихся в каждом из трех классов. 
# Выведите наименьшее число парт, которое нужно приобрести для них.
# Input: 20 21 22(ввод чисел НЕ в одну строку) Output: 32
# 15 минут

firstClass = int(input("Количество учеников в первом классе:  "))
secondClass = int(input("Количество учеников во втором классе:  "))
thirdClass = int(input("Количество учеников в третьем классе:  "))

tablesForFirst = firstClass// -2 # первый вариант
tablesForFirst = -tablesForFirst 
tablesForSecond = secondClass// 2 + secondClass%2 #второй вариант
tablesForThird = thirdClass// 2 + thirdClass%2
# tablesForThird = thirdClass// 3 + (thirdClass%3 != 0)  # третий вариант (универсальный по количеству > 2) 

print(tablesForFirst + tablesForSecond + tablesForThird)

 
