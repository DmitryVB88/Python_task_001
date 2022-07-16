# Напишите программу, которая принимает на вход координаты двух точек 
# и находит расстояние между ними в 2D пространстве.

x1 = int(input('Введите координату X1: '))
y1 = int(input('Введите координату Y1: '))
x2 = int(input('Введите координату X2: '))
y2 = int(input('Введите координату Y2: '))
print()
if y1 > y2:
    mult = (x2 - x1)**2 + (y1 - y2)**21
    print(mult)
else:
    mult = (x2 - x1)**2 + (y2 - y1)**2
    print(mult)
print()    
import math
sqrt = math.sqrt(mult)
print(sqrt)

