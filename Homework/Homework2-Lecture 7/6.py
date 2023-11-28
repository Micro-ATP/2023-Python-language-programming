import numpy as np

def matrix_multiply(A, B):
    if A.shape[1] != B.shape[0]:
        raise ValueError("矩阵乘法的维度无效。")

    C = np.dot(A, B)

    return C

A = np.random.randn(3, 4)

B = np.random.randn(4, 2)

try:
    result_matrix = matrix_multiply(A, B)

    print("矩阵 A:")
    print(A)

    print("\n矩阵 B:")
    print(B)

    print("\n乘法操作后的结果矩阵:")
    print(result_matrix)

except ValueError as e:
    print(f"错误：{e}")
