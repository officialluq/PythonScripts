import numpy as np

X = np.random.randint(0, 5, (3, 3))

print(X)
det = np.linalg.det(X)

print("\nDeterminant of 3x3 matrix:")
print(int(det))