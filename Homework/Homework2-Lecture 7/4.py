import numpy as np

oneDimArray = np.array([1, 2, 3, 4, 5])

twoDimArray = oneDimArray.reshape((5, 1))

expandedArray = np.expand_dims(twoDimArray, axis=1)


print("原始一维数组:")
print(oneDimArray)
print("\nReshape后的二维数组:")
print(twoDimArray)
print("\n在第二个维度上扩展后的数组:")
print(expandedArray)
