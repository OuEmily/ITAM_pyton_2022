
print ('Введите два числа')
a = str(input())
list = a.split()
list = [int (i) for  i in list]
start  = list[0]
end = list[1]
if end < start:
    end, start = start, end
def summation(start, end):
    s = 0
    for i in range(start, end + 1):
        s+=i
    print(s)
summation(start, end)
