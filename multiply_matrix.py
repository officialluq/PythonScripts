import numpy as np

X = np.random.randint(0, 2, (8, 8))

Y = np.random.randint(0, 2, (8, 8))

result = np.zeros((8,8))

for i in range(len(X)):
   for j in range(len(Y[0])):
       for k in range(len(Y)):
           result[i][j] += X[i][k] * Y[k][j]

for r in result:
   print(r)