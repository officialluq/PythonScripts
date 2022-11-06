import numpy as np


X = np.random.randint(0,100, (128,128))

Y = np.random.randint(0,100, (128,128))


result = np.zeros((128,128))
for i in range(len(X)):
   for j in range(len(X[0])):
       result[i][j] = X[i][j] + Y[i][j]


print(result)