import numpy as np

# 3.3.3.1 Устанавливаем «режим автоматических вычислений» 
np.set_printoptions(precision=3, suppress=True)
    # Сведения об исполнителе (можно также запросить с клавиатуры)
    fio = "Кукарин Артём Алексеевич"
    group_code = "Группа Скс-23"
    date_str = datetime.date.today().isoformat()

    # Открываем текстовый файл для записи
    with open("results.txt", "w", encoding="utf-8") as f:
        # Записываем шапку: ФИО, группа, дата
        f.write(f"Исполнитель: {fio}\n")
        f.write(f"Код группы: {group_code}\n")
        f.write(f"Дата выполнения работы: {date_str}\n")
        f.write("-" * 40 + "\n")
        f.write("   x    |     y\n")
        f.write("-" * 40 + "\n")

        print("\nРезультаты вычислений:\n")

# 3.3.3.2 Вводим матрицу P (3×3)
P = np.array([
    [0.587,  0.189, -0.455],
    [0.189,  0.913,  0.208],
    [-0.455, 0.208,  0.500]
])

print("Матрица P:")
print(P)

# 3.3.3.3 Вычисляем P^2 и (P^2 - P)
P2 = P @ P
print("\nP^2 =")
print(P2)

P2_minus_P = P2 - P
print("\nP^2 - P =")
print(P2_minus_P)

# 3.3.3.4 Вычисляем det(P) и P^-1
detP = np.linalg.det(P)
P_inv = np.linalg.inv(P)

print(f"\nОпределитель det(P) = {detP:.3f}")
print("\nОбратная матрица P^-1:")
print(P_inv)

# 3.3.3.5 Вводим единичную матрицу E той же размерности, что и P
E = np.eye(3)

print("\nЕдиничная матрица E:")
print(E)

# 3.3.3.6 Вычисляем матрицу I = 2P - E
I = 2 * P - E

print("\nМатрица I = 2P - E:")
print(I)

# 3.3.3.7 Вычисляем I^2
I2 = I @ I

print("\nI^2 =")
print(I2)

# 3.3.3.8 Вычисляем det(I) и I^-1
detI = np.linalg.det(I)
I_inv = np.linalg.inv(I)

print(f"\nОпределитель det(I) = {detI:.3f}")
print("\nОбратная матрица I^-1:")
print(I_inv)
