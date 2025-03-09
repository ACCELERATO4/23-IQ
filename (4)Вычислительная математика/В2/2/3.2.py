import numpy as np
A = np.array([
    [ 200,  -13,  12 ],
    [   1,  400,   9 ],
    [  -8,    8, 600 ]
], dtype=float)

b = np.array([
   -2470,
    904,
   7920
], dtype=float)

print("Матрица A:")
print(A)
print("\nВектор b:")
print(b)
#    Сначала найдём обратную матрицу A^(-1), затем умножим её на b.
A_inv = np.linalg.inv(A)  # обратная матрица
x_inv = A_inv @ b         # решение через умножение на A^(-1)
print("\nРешение, вычисленное через A^(-1) * b:")
print(x_inv)

#  правильность решения умножением A * x
check = A @ x_inv
print("\nПроверка решения A * x:")
print(check)
print("Сравнение с вектором b:")
print(b)
x_solve = np.linalg.solve(A, b)
print("\nРешение через np.linalg.solve(A, b):")
print(x_solve)

print("\nСравнение решений:")
print("Через A^(-1)*b =", x_inv)
print("Через linalg.solve =", x_solve)
