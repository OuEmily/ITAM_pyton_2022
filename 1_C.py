def summation(*chislo):
    A = list(chislo)
    s = 0
    B = []
    for i in range (len(A)):
        if A[i] < 0:
            A[i] *= -2
    print(A)
    max = A[0]
    for i in range (len(A)):
        if A[i] > max:
            max = A[i]
    for i in range (len(A)):
        A[i] = A[i]/max
        s += A[i]
    print(s)
summation(-10, 2, 3, 15, -4)