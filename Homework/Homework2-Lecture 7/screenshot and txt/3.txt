import numpy as np  

twoDimArray = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])  

print("二维数组：")  
print(twoDimArray)

oneDimArray = twoDimArray.ravel()  
print("一维数组：")  
print(oneDimArray)