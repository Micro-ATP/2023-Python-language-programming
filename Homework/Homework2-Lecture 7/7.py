import numpy as np

np.random.seed(42)

num_samples = 1000 
num_features = 5    

X = np.random.randn(num_samples, num_features)

y = np.random.randint(2, size=num_samples)

print("Feature Matrix (X):")
print(X[:5])
print("\nTarget Vector (y):")
print(y[:5])
