import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp

# Параметры задачи
N = 12
K = 0.01 * N
omega_squared = 0.77

# Начальные условия
y0 = [1, 0.1]  # y(0) = 1, y'(0) = 0.1

# Функция, задающая систему дифференциальных уравнений
def system(t, y):
    y1, y2 = y
    dy1dt = y2
    dy2dt = 2 * K * y2 + y1 * omega_squared
    return [dy1dt, dy2dt]

# Параметры решения
t0 = 0
t_end = 10
h = 0.1
t_eval = np.arange(t0, t_end + h, h)  # Узлы сетки

# Решение системы с использованием solve_ivp (аналог rkfixed)
sol = solve_ivp(system, [t0, t_end], y0, t_eval=t_eval, method='RK45')

# Сохранение решения в матрицу (аналог rkfixed)
# Матрица Y будет содержать t, y(t), y'(t)
Y = np.column_stack((sol.t, sol.y[0], sol.y[1]))

# Вывод таблицы решений
print("Таблица решений:")
print("t\t\t y(t)\t\t y'(t)")
for row in Y:
    print(f"{row[0]:.2f}\t {row[1]:.6f}\t {row[2]:.6f}")

# Построение графика
plt.figure(figsize=(10, 6))
plt.plot(sol.t, sol.y[0], label='y(t)')
plt.plot(sol.t, sol.y[1], label="y'(t)", linestyle='--')
plt.xlabel('t')
plt.ylabel('y, y\'')
plt.title('Решение дифференциального уравнения методом Рунге-Кутта (аналог rkfixed)')
plt.legend()
plt.grid(True)
plt.show()