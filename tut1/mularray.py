import random

X_SIZE = 3
Y_SIZE = 4

matrix = [[0 for x in range(Y_SIZE)] for x in range(X_SIZE)]
for i in range(X_SIZE):
    for j in range(Y_SIZE):
        matrix[i][j] = (random.randint(100, 1000))
        print( matrix[i][j] )
    print( matrix[i] )
