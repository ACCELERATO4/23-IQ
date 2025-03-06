import numpy as np

np.set_printoptions(precision=2, suppress=True)
ORIGIN = 1
A = np.array([
    [2.0,   1.0,   2.0,    1.0   ],
    [6.0,   0.0,   4.0,    0.5   ],
    [2.5,   1.333, 0.6667, 0.693 ],
    [4.4,   1.5,  -2.667,  2.0   ]
])
# Берём второй столбец (индекс 1) в качестве V
V = A[:, 1]
# Единичная матрица 4×4
E = np.eye(4)
# Возьмём ещё три вектора из E — e2, e3, e4
e2 = E[:, 1]
e3 = E[:, 2]
e4 = E[:, 3]
# Функция Грама–Шмидта для ортонормировки
def gram_schmidt(vecs):
    ortho = []
    for v in vecs:
        w = v.copy()
        for u in ortho:
            w -= np.dot(u, w) * u
        norm_w = np.linalg.norm(w)
        if norm_w < 1e-14:
            raise ValueError("Один из векторов оказался слишком мал (почти ноль) после ортогонализации.")
        w = w / norm_w
        ortho.append(w)
    return ortho


vectors = [V, e2, e3, e4]
orthonormal_basis = gram_schmidt(vectors)
H = np.column_stack(orthonormal_basis)
print("Матрица H:")
print(H)
HTH = H.T @ H
HHT = H @ H.T
print("\nH^T * H =")
print(HTH)
print("\nH * H^T =")
print(HHT)
H_inv = np.linalg.inv(H)
print("\nH^-1 =")
print(H_inv)
difference = np.linalg.norm(H_inv - H.T)
print(f"\nСравнение H^-1 и H^T: норма разности = {difference:e}")
detH = np.linalg.det(H)
print(f"\nОпределитель det(H) = {detH:.2f}")

print("\nВыводы:")
print("1) Если H^T*H и H*H^T близки к единичной матрице, столбцы H – ортонормированные вектора.")
print("2) Если H^-1 близка к H^T, значит H – ортогональная матрица.")
print("3) Если det(H) = 1, то H – ортогональная матрица с положительной ориентацией (вращение).")
