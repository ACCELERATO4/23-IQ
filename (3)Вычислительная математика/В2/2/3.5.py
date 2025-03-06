import numpy as np
import sympy as sp

# 1. Установим режим автоматических вычислений (используем numpy и sympy)
sp.init_printing()

# 2. Введем матрицу системы A и векторы b1, b2
A = np.array([
    [-13, -8, -3, 2, 7],
    [0, -1, 7, -3, -13],
    [-13, -8, 3, 4, -1],
    [-13, -9, 4, -1, -6],
    [-26, -17, 7, 3, -7]
])

b1 = np.array([-2.8, -26.3, -16.8, -29.1, -45.9]).reshape(-1, 1)
b2 = np.array([-1.8, -26.1, -15.8, -29.77, -46.9]).reshape(-1, 1)

# Расширенные матрицы
Ab1 = np.hstack((A, b1))
Ab2 = np.hstack((A, b2))

# 3. Вычислим ранги основной матрицы и расширенных матриц
rank_A = np.linalg.matrix_rank(A)
rank_Ab1 = np.linalg.matrix_rank(Ab1)
rank_Ab2 = np.linalg.matrix_rank(Ab2)

# 4. Формулируем вывод
if rank_A == rank_Ab1 and rank_A == rank_Ab2:
    conclusion = "Система совместна для обеих правых частей."
    if rank_A < A.shape[1]:
        conclusion += " Система имеет бесконечно много решений."
    else:
        conclusion += " Система имеет единственное решение."
elif rank_A == rank_Ab1:
    conclusion = "Система совместна только для b1, но несовместна для b2."
elif rank_A == rank_Ab2:
    conclusion = "Система совместна только для b2, но несовместна для b1."
else:
    conclusion = "Система несовместна для обеих правых частей."

# 5. Приведем расширенные матрицы к ступенчатому виду
Ab1_reduced = sp.Matrix(Ab1).rref()[0]
Ab2_reduced = sp.Matrix(Ab2).rref()[0]

# 6. Определим базисные и свободные переменные
_, pivots_b1 = sp.Matrix(Ab1).rref()
_, pivots_b2 = sp.Matrix(Ab2).rref()

basis_vars_b1 = list(pivots_b1)
free_vars_b1 = list(set(range(A.shape[1])) - set(basis_vars_b1))

basis_vars_b2 = list(pivots_b2)
free_vars_b2 = list(set(range(A.shape[1])) - set(basis_vars_b2))

# 7-8. Записываем эквивалентную систему и общее решение
A_sym = sp.Matrix(A)
b1_sym = sp.Matrix(b1)
b2_sym = sp.Matrix(b2)

# 9. Найдем два частных решения (если есть свободные переменные)
particular_solutions = []
if free_vars_b1:
    for i in free_vars_b1[:2]:  # Берем два первых свободных
        x_part = sp.zeros(A.shape[1], 1)
        x_part[i] = 1
        particular_solutions.append(x_part)

# 10. Проверка решений с использованием метода Гаусса (rref)
def check_solution(A, b):
    Ab = A.row_join(b)  # Расширенная матрица
    rref_matrix, pivots = Ab.rref()  # Приведение к ступенчатому виду
    rank_A = A.rank()
    rank_Ab = Ab.rank()
    
    return rank_A == rank_Ab  # Совместность системы

# Проверяем решения
validity_b1 = check_solution(A_sym, b1_sym)
validity_b2 = check_solution(A_sym, b2_sym)

# Красивый форматированный вывод
print("=" * 50)
print("РЕЗУЛЬТАТЫ РЕШЕНИЯ СИСТЕМЫ ЛИНЕЙНЫХ УРАВНЕНИЙ".center(50))
print("=" * 50)

# Вывод рангов
print(f"\nРанг основной матрицы A: {rank_A}")
print(f"Ранг расширенной матрицы A|b1: {rank_Ab1}")
print(f"Ранг расширенной матрицы A|b2: {rank_Ab2}")

# Вывод заключения
print("\nВывод:")
print(conclusion)

# Вывод базисных и свободных переменных
print("\nБазисные и свободные переменные:")
print(f"Базисные переменные (b1): {basis_vars_b1}")
print(f"Свободные переменные (b1): {free_vars_b1}")
print(f"Базисные переменные (b2): {basis_vars_b2}")
print(f"Свободные переменные (b2): {free_vars_b2}")

# Вывод ступенчатых матриц в удобном формате
print("\nПриведенная форма A|b1:")
sp.pprint(Ab1_reduced)

print("\nПриведенная форма A|b2:")
sp.pprint(Ab2_reduced)

# Вывод частных решений (если они есть)
if particular_solutions:
    print("\nЧастные решения (для b1):")
    for idx, sol in enumerate(particular_solutions, 1):
        print(f"\nЧастное решение {idx}:")
        sp.pprint(sol)

# Проверка решений
print("\nПроверка решений:")
print(f"Проверка для b1: {'Корректно' if validity_b1 else 'Ошибка (система несовместна)'}")
print(f"Проверка для b2: {'Корректно' if validity_b2 else 'Ошибка (система несовместна)'}")

# Разделитель в конце
print("=" * 50)
