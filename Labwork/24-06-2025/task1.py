matrix = [[1, 2], [3, 4], [5, 6]]
print(matrix)
matrix.remove([3, 4])
print(matrix)
matrix.pop(0)
print(matrix)
matrix[0].remove(6)
print(matrix)
matrix.append(20)
print(matrix)
matrix.append([21,22,23,24])
print(matrix)
matrix[2].append(25)
print(matrix)
matrix.append([10,20,30])
print(matrix)
matrix.insert(2, [11, 12, 13])
print(matrix)

for i in range(1,3):
    pass
print(matrix[3])
matrix[1]=10
print(matrix)