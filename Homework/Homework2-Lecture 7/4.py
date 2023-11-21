import numpy as np

one_dim_array = np.array([1, 2, 3, 4, 5])

two_dim_array = one_dim_array.reshape((5, 1))

expanded_array = np.expand_dims(two_dim_array, axis=1)

# 输出结果
print("原始一维数组:")
print(one_dim_array)
print("\nReshape后的二维数组:")
print(two_dim_array)
print("\n在第二个维度上扩展后的数组:")
print(expanded_array)
