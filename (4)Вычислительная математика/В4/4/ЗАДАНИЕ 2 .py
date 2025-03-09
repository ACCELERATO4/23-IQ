import numpy as np
import matplotlib.pyplot as plt

# Определение функции правой части дифференциального уравнения
def f(x, y):
    return -y * np.log(y) / x

# Метод Рунге-Кутта 4-го порядка
def runge_kutta(f, x0, y0, h, x_end):
    x_values = np.arange(x0, x_end + h, h)
    y_values = []
    y = y0
    for x in x_values:
        y_values.append(y)
        k1 = h * f(x, y)
        k2 = h * f(x + h/2, y + k1/2)
        k3 = h * f(x + h/2, y + k2/2)
        k4 = h * f(x + h, y + k3)
        y = y + (k1 + 2*k2 + 2*k3 + k4) / 6
    return x_values, y_values

# Начальные условия и параметры
x0 = 1
y0 = np.e
x_end = 6
h = 0.1

# Вычисление решений с разными шагами
x1, y1 = runge_kutta(f, x0, y0, h, x_end)
x2, y2 = runge_kutta(f, x0, y0, 2*h, x_end)
x3, y3 = runge_kutta(f, x0, y0, h/2, x_end)

# Создание фигуры с увеличенным размером
plt.figure(figsize=(12, 6))  # Ширина: 12, Высота: 6

# Построение графиков
plt.plot(x1, y1, label=f'Шаг h={h}', linewidth=2)
plt.plot(x2, y2, label=f'Шаг 2h={2*h}', linestyle='--', linewidth=2)
plt.plot(x3, y3, label=f'Шаг h/2={h/2}', linestyle=':', linewidth=2)

# Настройка осей и заголовка
plt.xlabel('x', fontsize=12)
plt.ylabel('y', fontsize=12)
plt.title('Решение задачи Коши методом Рунге-Кутта', fontsize=14)

# Добавление легенды и сетки
plt.legend(fontsize=12)
plt.grid(True)

# Отображение графика
plt.show()