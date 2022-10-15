
def greetings():
    print("Введите имя и фамилию")
    a = str(input())
    list = a.split() 
    print('Доброго времени суток,',  list[0] , '"Человек"' ,  list[1] , sep = '  ', end ='!')
greetings()