import numpy as np

oneDimArray = np.array([1, 2, 3, 4, 5])  

twoDimArray = np.expand_dims(oneDimArray, axis=1)  

print(twoDimArray)