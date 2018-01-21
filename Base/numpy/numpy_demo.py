from numpy import *


def printLine():
    for i in range(0, 100):
        print('-', end='')
    print()


arr = random.rand(4, 4)
print(arr)
printLine()

randMat = mat(random.rand(4, 4))
print(randMat)
printLine()

invRandMat = randMat.I
print(invRandMat)
printLine()

print(randMat * invRandMat)
printLine()