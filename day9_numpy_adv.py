# Day 9 - NumPy Advanced
# Raj Gajare | Prime 2.0

import numpy as np

# ✅ Part 1 - Broadcasting
print("=== Broadcasting ===")
arr = np.array([1, 2, 3, 4, 5])
print("Original:", arr)
print("Add 10:", arr + 10)
print("Multiply 2:", arr * 2)

matrix = np.array([[1, 2, 3],
                   [4, 5, 6],
                   [7, 8, 9]])
print("\nMatrix + [10,20,30]:")
print(matrix + np.array([10, 20, 30]))

# ✅ Part 2 - Boolean Indexing
print("\n=== Boolean Indexing ===")
marks = np.array([85, 45, 92, 38, 78, 55, 95])
print("All marks:", marks)
print("Passing (>60):", marks[marks > 60])
print("Failed (<60):", marks[marks < 60])
print("Between 70-90:", marks[(marks >= 70) & (marks <= 90)])

# ✅ Part 3 - np.where
print("\n=== np.where ===")
result = np.where(marks >= 60, "Pass", "Fail")
print("Results:", result)

grades = np.where(marks >= 90, "A",
         np.where(marks >= 75, "B",
         np.where(marks >= 60, "C", "F")))
print("Grades:", grades)

# ✅ Part 4 - Matrix Multiplication
print("\n=== Matrix Multiplication ===")
a = np.array([[1, 2],
              [3, 4]])
b = np.array([[5, 6],
              [7, 8]])

print("Matrix A:\n", a)
print("Matrix B:\n", b)
print("A dot B:\n", np.dot(a, b))
print("Element wise:\n", a * b)

# ✅ Part 5 - Random Module
print("\n=== Random ===")
np.random.seed(42)
print("Random integers:", np.random.randint(1, 100, 5))
print("Random floats:", np.random.random(5).round(2))
print("Normal dist:", np.random.normal(0, 1, 5).round(2))

# Random matrix
random_matrix = np.random.randint(1, 50, (3, 3))
print("\nRandom 3x3 Matrix:\n", random_matrix)
print("Row wise sum:", random_matrix.sum(axis=1))
print("Col wise sum:", random_matrix.sum(axis=0))