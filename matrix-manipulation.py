def add_matrix(arr1, arr2):
    result = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
    for i in range(0, len(arr1)):
        for j in range(0, len(arr1[i])):
            result[i][j] = arr1[i][j] + arr2[i][j]
    return result;

a = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
b = [[9, 8, 7], [6, 5, 4], [3, 2, 1]]

print(add_matrix(a,b))