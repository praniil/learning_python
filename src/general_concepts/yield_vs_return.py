def fun(number):
    for i in range(number):
        yield i * i     #returns a generator
    
def fun1(number):
    for i in range(number):
        return i * i

gen = fun(3)
print(next(gen))
print(fun1(3))
print(next(gen))

#normal list
square_list = [x ** 2 for x in range(1, 5)]
#generator
square_list_gen = (x ** 2 for x in range(1, 5))

print(square_list)
print(next(square_list_gen))
print(next(square_list_gen))
print(next(square_list_gen))
print(next(square_list_gen))
