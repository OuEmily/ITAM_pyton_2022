
def system(n,k):
    ost = '0123456789ABCDEFGHIGKLMNOPQRSTUVWXYZ'
    result = ' '
    while n > k:
     first = n % k  
     result = ost[first] + result
     n = n // k
    result = ost[n] + result
    print(result)
system(1234,8)