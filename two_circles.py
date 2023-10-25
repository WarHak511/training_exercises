import matplotlib.pyplot as plt
import numpy as np

theta = np.linspace(0, 2 * np.pi, 100)

# Координаты x и y для окружности радиусом 1 с центром в (0,0)
x1 = np.cos(theta)
y1 = np.sin(theta)

# Координаты x и y для окружности радиусом 1 с центром в (-1,0)
x2 = np.cos(theta) - 1
y2 = np.sin(theta)   # Смещаем центр окружности вниз на 1 по оси ординат

# Строим графики окружностей и осей
plt.figure(figsize=(6, 6))  # чтобы график был круглым
plt.plot(x1, y1, label="Окружность (0,0) радиусом 1")
plt.plot(x2, y2, label="Окружность (-1,0) радиусом 1")
intersection_x = np.linspace(-1, 0, 100)
intersection_y = np.sqrt(1 - (intersection_x + 1)**2)
intersection_z = np.sqrt(1 - (intersection_x)**2)
plt.fill_between(intersection_x, -intersection_y, intersection_y,
                 -intersection_z, color='red', alpha=0.3)
plt.axhline(0, color='black', linewidth=2)  # Горизонтальная ось (x)
plt.axvline(0, color='black', linewidth=2)  # Вертикальная ось (y)
plt.xlabel("X")
plt.ylabel("Y")
plt.title("Окружности с центрами в (0,0) и (-1,0) радиусом 1")
plt.legend()
plt.grid(True)
# устанавливаем равное масштабирование осей
# для корректного отображения окружностей
plt.gca().set_aspect('equal', adjustable='datalim')
plt.show()
