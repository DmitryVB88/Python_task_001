# Напишите программу, которая принимает на вход цифру, обозначающую день недели, 
# и проверяет, является ли этот день выходным.

a = int(input('Ввелите число от 1 до 7. \nКаждое число соответствует дню недели: '))
if 0 < a < 6:
      print('Этот день является рабочим')
elif a == 6 or a == 7:
      print('А в этот день, можно и отдыхать! Выходной, понимаешь!')
else:
      print('Данный диапазон не входит в дни недели.')