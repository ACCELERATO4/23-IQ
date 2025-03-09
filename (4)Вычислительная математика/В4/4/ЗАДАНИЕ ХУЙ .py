import numpy as np
import matplotlib.pyplot as plt
from scipy.linalg import expm

# 1. Присвойте переменной ORIGIN значение, равное единице.
# В Python индексация начинается с 0, но для матриц и массивов это не требуется.

# 2. Введите начальные условия и значения H.
A = np.array([
    [22.6, 47.6, 29.6, 27.8],
    [-26.8, -22.0, -20.0, -16.8],
    [-4.6, -17.0, -10.0, -9.6],
    [2.2, -27.6, -9.6, -13.0]
])
y0 = np.array([0.909, -0.416, -0.654, -0.757])

# 3. Выберите значение шага h.
h = 0.01  # Шаг
H = 1.0  # Интервал для матричной экспоненты

# 4. Вычислите матричную экспоненту e^(A*h) с использованием разложения в ряд Тейлора.
def matrix_exponential_taylor(A, h, order=10):
    exp_Ah = np.eye(A.shape[0])  # Начальное значение: единичная матрица
    A_power = np.eye(A.shape[0])  # Начальное значение: A^0
    for k in range(1, order + 1):
        A_power = A_power @ (A * h) / k  # A^k * h^k / k!
        exp_Ah += A_power
    return exp_Ah

exp_Ah = matrix_exponential_taylor(A, h)

# 5. Вычислите матричную экспоненту e^(A*H).
exp_AH = matrix_exponential_taylor(A, H)

# 6. Вычислите приближенное решение задачи Коши в указанных точках и постройте график.
def solve_cauchy(A, y0, h, t_end):
    t_values = np.arange(0, t_end + h, h)
    y_values = []
    y = y0
    for t in t_values:
        y_values.append(y)
        y = exp_Ah @ y  # Применяем матричную экспоненту
    return t_values, np.array(y_values)

t_end = 1.0  # Конечное время
t_values, y_values = solve_cauchy(A, y0, h, t_end)

# Построение графика
plt.figure(figsize=(10, 6))
for i in range(y_values.shape[1]):
    plt.plot(t_values, y_values[:, i], label=f'y{i+1}(t)')
plt.xlabel('t')
plt.ylabel('y(t)')
plt.title('Приближенное решение задачи Коши методом матричной экспоненты')
plt.legend()
plt.grid(True)
plt.show()

# 7. Найдите решение задачи Коши на указанном промежутке, используя стандартные функции SciPy.
from scipy.integrate import solve_ivp

def system(t, y):
    return A @ y

sol = solve_ivp(system, [0, t_end], y0, t_eval=t_values, method='BDF')  # Используем метод для жестких систем

# Построение графика
plt.figure(figsize=(10, 6))
for i in range(sol.y.shape[0]):
    plt.plot(sol.t, sol.y[i], label=f'y{i+1}(t)', linestyle='--')
plt.xlabel('t')
plt.ylabel('y(t)')
plt.title('Решение задачи Коши с использованием SciPy (BDF)')
plt.legend()
plt.grid(True)
plt.show()

# 8. Сравните полученные графики.
# Графики уже построены выше, их можно визуально сравнить.