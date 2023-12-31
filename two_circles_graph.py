# Исходными данными являются координаты точки
# M (x, y). Составьте программу, которая определяет,
# принадлежит ли точка М области пересечения окружностей
# с центрами в точках с координатами (-1,0) и (0, 0)

import math

# Координаты центров окружностей и их радиус
center1 = (-1, 0)
center2 = (0, 0)
radius = 1

# Ввод координат точки M
x_m = float(input("Введите координату x для точки M: "))
y_m = float(input("Введите координату y для точки M: "))

# Расстояния от точки M до центров окружностей
distance1 = math.sqrt((x_m - center1[0])**2 + (y_m - center1[1])**2)
distance2 = math.sqrt((x_m - center2[0])**2 + (y_m - center2[1])**2)

# Проверка вхождения точки M в область пересечения
if distance1 <= radius and distance2 <= radius:
    print("Точка M входит в область пересечения двух окружностей.")
else:
    print("Точка M не входит в область пересечения двух окружностей.")
