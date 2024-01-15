#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    Newsquare = []
    a = 0
    for x in matrix:
        Newsquare.append([])
        for y in matrix[a]:
            Newsquare[a].append(y**2)
        a += 1
    return (Newsquare)
