import math
def stairs():
    print(" Введите количество блоков")
    print ("n = ")
    n = int(input())
    N = (-1 + math.sqrt(1 + 8*n)) // 2
    print (N)
stairs()