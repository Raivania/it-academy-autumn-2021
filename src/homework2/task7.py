side1 = int(input('Введите первую сторону: '))
side2 = int(input('Введите вторую сторону: '))
side3 = int(input('Введите третью сторону: '))
p = side1 + side2 + side3
if side1 + side2 <= side3:
    print('Это не треугольник')
else:
    print('Площадь треугольника = ', (p * (p - side1) + (p - side2) + (p - side3)) ** 0.5)
