def fun(number):
    for i in range(number):
        yield i * i
    
def fun1(number):
    for i in range(number):
        return i * i

list = list(fun(7))     #outputs list of squares of number upto 6
print(list)

list2 = fun1(7)
print(list2)    #outputs 0
    