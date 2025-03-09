import numpy as np
import matplotlib.pyplot as plt

# Определение функции правой части дифференциального уравнения
def f(x, y):
    return 0.185 * (x**2 + np.cos(0.7 * x)) + 1.843 * y

# Параметры задачи
x0 = 0.2
y0 = 0.25
h = 0.2
x_end = 2.0

# Метод Эйлера-Коши
def euler_cauchy(f, x0, y0, h, x_end):
    x_values = np.arange(x0, x_end + h, h)
    y_values = []
    y = y0
    for x in x_values:
        y_values.append(y)
        y_pred = y + h * f(x, y)
        y = y + h * (f(x, y) + f(x + h, y_pred)) / 2
    return x_values, y_values

# Вычисление решения
x_values, y_values = euler_cauchy(f, x0, y0, h, x_end)

# Вывод таблицы решений
print("x\t y")
for x, y in zip(x_values, y_values):
    print(f"{x:.1f}\t {y:.6f}")

# Построение графика
plt.plot(x_values, y_values, marker='o')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Решение задачи Коши методом Эйлера-Коши')
plt.grid(True)
plt.show()