import numpy as np

def matrix_multiply(A, B):
    """
    对两个矩阵 A 和 B 执行矩阵乘法。

    参数：
    - A: 第一个矩阵，形状为 (m, n)
    - B: 第二个矩阵，形状为 (n, p)

    返回值：
    - C: 结果矩阵，形状为 (m, p)
    """

    # 检查 A 的列数是否等于 B 的行数
    if A.shape[1] != B.shape[0]:
        raise ValueError("矩阵乘法的维度无效。")

    # 使用 np.dot 或 @ 运算符执行矩阵乘法
    C = np.dot(A, B)
    # 或者，你可以在 Python 3.5 及更高版本中使用 @ 运算符：
    # C = A @ B

    return C

# 示例用法：
# 假设矩阵 A 和 B 是具有适当形状的随机生成的
# 你可以使用 np.random.randn 生成随机矩阵

# 定义形状为 (m, n) 的矩阵 A
A = np.random.randn(3, 4)

# 定义形状为 (n, p) 的矩阵 B
B = np.random.randn(4, 2)

try:
    # 调用矩阵乘法的函数
    result_matrix = matrix_multiply(A, B)

    # 打印矩阵和结果
    print("矩阵 A:")
    print(A)

    print("\n矩阵 B:")
    print(B)

    print("\n乘法操作后的结果矩阵:")
    print(result_matrix)

except ValueError as e:
    print(f"错误：{e}")
