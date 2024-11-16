import numpy as np
A = np.random.randint(1, 10, size=(9, 9))
a_sum_for = 0

for j in range(9):
    a_sum_for += A[0, j]
    a_sum_for += A[8, j]

for i in range(1, 8):
    a_sum_for += A[i, 0]
    a_sum_for += A[i, 8]
print(A)
print(a_sum_for)
