import numpy as np
image_data = np.random.rand(1000,28,28)

reshaped_image_data = image_data.reshape(-1,28,28,1)
