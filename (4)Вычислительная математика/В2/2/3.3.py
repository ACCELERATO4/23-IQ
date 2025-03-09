import numpy as np
np.set_printoptions(suppress=True, precision=4)
ORIGIN = 1
A = np.array([
    [ 200,  -13,   12 ],
    [   1,  400,    9 ],
    [  -8,    8,  600 ]
], dtype=float)

b = np.array([
   -2470,
    904,
   7920
], dtype=float)

print("Матрица A:")
print(A)
print("\nСтолбец правых частей b:")
print(b)    

Ab = np.hstack((A, b.reshape(-1, 1)))
print("\nРасширенная матрица [A|b]:")
print(Ab)
# Приведите расширенную матрицу к ступенчатому виду
n = len(b)
for i in range(n):
    # Находим ведущий элемент
    pivot = i + np.argmax(np.abs(Ab[i:, i]))
    if abs(Ab[pivot, i]) < 1e-15:
        print("\nСистема, вероятно, вырождена (pivot = 0). Единственное решение не гарантируется.")
        break
    
    # Меняем строки i и pivot
    if pivot != i:
        Ab[[i, pivot], :] = Ab[[pivot, i], :]

    # Зануляем элементы ниже ведущего
    for j in range(i+1, n):
        factor = Ab[j, i] / Ab[i, i]
        Ab[j, i:] -= factor * Ab[i, i:]

print("\nРасширенная матрица [A|b] после приведения к ступенчатому виду:")
print(Ab)

#  Сформируйте столбец решения (обратный ход)
x = np.zeros(n)
for i in range(n-1, -1, -1):
    x[i] = Ab[i, -1]
    for j in range(i+1, n):
        x[i] -= Ab[i, j] * x[j]
    x[i] /= Ab[i, i]

print("\nСтолбец решения x, найденный методом Гаусса:")
print(x)

# 7. Проверка решения умножением матрицы системы на вектор x
check = A @ x
print("\nПроверка решения (A * x):")
print(check)
print("\nСравнение с исходным столбцом b:")
print(b)
