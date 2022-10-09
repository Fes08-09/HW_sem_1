# Задача 4. Напишите программу, которая по заданному номеру четверти, показывает диапазон возможных координат точек в этой четверти (x и y).

numberOfQuarter = int(input('Введите номер четверти (от 1 до 4): '))

if numberOfQuarter > 4 or numberOfQuarter < 1:
    print('Введен некорректный номер четверти')
    

if numberOfQuarter == 1:
    print('Диапазон возможных координат Х > 0; Y > 0')
elif numberOfQuarter == 2:
    print('Диапазон возможных координат Х < 0; Y > 1')
elif numberOfQuarter == 3:
    print('Диапазон возможных координат Х < 0; Y < 0')
elif numberOfQuarter == 4:
    print('Диапазон возможных координат Х > 0; Y < 0')


