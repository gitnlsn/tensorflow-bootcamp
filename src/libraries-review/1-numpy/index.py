import numpy as np

print("=== Creating Arrays ===")
arr = np.array([0,1,2,3,4])
print("np array", arr)

my_list = [0,1,2,3,4]
arr = np.array(my_list)
print("arr from list:", arr)

result = np.arange(0,10)
print("np.arange(0,10):", result)

result = np.arange(0,10,2)
print("np.arange(0,10,2):", result)

result = np.zeros((5,5))
print("np.zeros((5,5)):\n", result)

result = np.ones((2,4))
print("np.ones((2,4)):\n", result)

result = np.random.randint(0,10)
print("np.random.randint(0,10):", result)

result = np.random.randint(0,10,(3,3))
print("np.random.randint(0,10,(3,3)):\n", result)

result = np.linspace(0,10,6)
print("np.linspace(0,10,6):", result)

result = np.linspace(0,10,101)
print("np.linspace(0,10,101):", result)

print("\n=== Operations ===")
np.random.seed(101)
arr = np.random.randint(0,100,10)
print("arr:", arr)

arr2 = np.random.randint(0,100,10)
print("arr2:", arr2)

print("arr.max():", arr.max())
print("arr.min():", arr.min())
print("arr.mean():", arr.mean())
print("arr.argmin():", arr.argmin())
print("arr.argmax():", arr.argmax())

result = arr.reshape(2,5)
print("arr.reshape(2,5):\n", result)

print("\n=== Indexing ===")
mat = np.arange(0,100).reshape(10,10)
print("mat:\n", mat)

row = 0
col = 1
print(f"mat[{row},{col}]:", mat[row,col])

print(f"mat[:,{col}] (column {col}):", mat[:,col])
print(f"mat[{row},:] (row {row}):", mat[row,:])

result = mat[0:3,0:3]
print("mat[0:3,0:3]:\n", result)

print("\n=== Masking ===")
mask = mat > 50
print("mat > 50:\n", mask)

filtered = mat[mat>50]
print("mat[mat>50]:", filtered)