import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp

# 1. Установите режим автоматических вычислений.
# В Python это подразумевается по умолчанию.

# 2. Присвойте переменной ORIGIN значение, равное единице.
# В Python индексация начинается с 0, но для матриц и массивов это не требуется.

# 3. Присвойте начальное значение решения вектору-столбцу с именем Y.
Y0 = [0, 1]  # y1(0) = 0, y2(0) = 1

# 4. Определите правую часть уравнения, присвойте соответствующие выражения элементам вектора-столбца с именем f(x, y).
def system(x, y):
    y1, y2 = y
    dy1dx = np.cos(x**2 + y2**2)
    dy2dx = np.sin(x + y1)
    return [dy1dx, dy2dx]

# 5. Найдите величину N = [(x0 - x1) / h].
a = 0  # Начало отрезка
b = 2  # Конец отрезка
h = 0.1  # Шаг
N = int((b - a) / h)  # Количество шагов

# 6. Вычислите решение, используя функцию solve_ivp (аналог rkfixed) с параметром N.
sol1 = solve_ivp(system, [a, b], Y0, t_eval=np.linspace(a, b, N + 1), method='RK45')

# 7. Сохраните решение в матрице Y1.
Y1 = np.column_stack((sol1.t, sol1.y[0], sol1.y[1]))

# 8. Вычислите решение, используя функцию solve_ivp с параметром N = [(|x_end - x0|) / (2h)].
N2 = int((b - a) / (2 * h))
sol2 = solve_ivp(system, [a, b], Y0, t_eval=np.linspace(a, b, N2 + 1), method='RK45')

# 9. Сохраните решение в матрице Y2.
Y2 = np.column_stack((sol2.t, sol2.y[0], sol2.y[1]))

# 10. Вычислите решение, используя функцию solve_ivp с параметром N = [(|x_end - x0|) / (2h)].
# (Повторяем шаг 8 для Y3)
N3 = int((b - a) / (2 * h))
sol3 = solve_ivp(system, [a, b], Y0, t_eval=np.linspace(a, b, N3 + 1), method='RK45')

# 11. Сохраните решение в матрице Y3.
Y3 = np.column_stack((sol3.t, sol3.y[0], sol3.y[1]))

# 12. Постройте на одном графике все три найденные решения.
plt.figure(figsize=(10, 6))
plt.plot(Y1[:, 0], Y1[:, 1], label='y1(x), h=0.1', linestyle='-', marker='o')
plt.plot(Y2[:, 0], Y2[:, 1], label='y1(x), h=0.2', linestyle='--', marker='x')
plt.plot(Y3[:, 0], Y3[:, 1], label='y1(x), h=0.2', linestyle=':', marker='s')
plt.xlabel('x')
plt.ylabel('y1(x)')
plt.title('Решение системы дифференциальных уравнений')
plt.legend()
plt.grid(True)
plt.show()

# 13. Оцените погрешности найденных решений по формуле Рунге.
# Формула Рунге для оценки погрешности: |Y1 - Y2| / (2^k - 1), где k — порядок метода (для RK45 k=4)
runge_error = np.abs(Y1[:, 1] - Y2[:, 1]) / (2**4 - 1)
print("Оценка погрешности по формуле Рунге:")
print(runge_error)