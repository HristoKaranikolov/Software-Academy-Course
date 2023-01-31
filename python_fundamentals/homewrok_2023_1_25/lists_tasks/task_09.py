# Write a program, that creates quadratic form of a matrix,
# with a given number from the console.
# Example: number  = 4
# Result:
# [1, 5, 9, 13]
# [2, 6, 10, 14]
# [3, 7, 11, 15]
# [4, 8, 12, 16]


def read_matrix(num):
    matrix = []
    for i in range(1, num + 1):
        matrix.append([])
        for j in range(i, (num * num + 1), num):
            matrix[i - 1].append(j)

    return matrix


number = int(input('Enter a number '))
print('\n'.join([str(x) for x in read_matrix(number)]))
