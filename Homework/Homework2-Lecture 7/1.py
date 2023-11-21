import numpy as np  

one_dim_array = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])  
  
# Convert the one-dimensional array into a 3x4 two-dimensional array  
two_dim_array = np.reshape(one_dim_array, (3, 4))  
  
# Output the result  
print(two_dim_array)