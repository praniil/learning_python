# GENERIC FUNCTIONS
list_int = [1, 2,3 , 4, 5]
list_str = ["hellow", "world","hello"]

def take_list(list_arg):
    return list_arg[0]

first = take_list(list_int) #at this point pythod doesnt konw which type did the func return

#using type hints without generics
def first(items: list):
    return items[0]

first_item = first(list_str) #at this point we know the argument is of type list but not the type of return

#lets use generics
# we use generics in this case becasue the return type is same as the type inside the list given as an argument
from typing import TypeVar
from typing import Generic

T = TypeVar("T")    #T is not a var that consists of something it only exists just for type checking
def give_first(items:list[T]) -> T:
    return items[0]

first_int = give_first(list_int)
first_string = give_first(list_str)

print(first_int)
print(first_string) 


#GENERIC CLASSES
box_types = TypeVar("box_types")

class Box(Generic[box_types]):
    def __init__(self, obj: type[box_types]):
        self.obj = obj

    def get(self) -> box_types:
        return self.obj 

class Rectangle():
    length = 10
    breadth = 12
    
    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth

class ReturnRectangle(Box[Rectangle]):
    def __init__(self):
        super().__init__(Rectangle)

ret_rect = ReturnRectangle()
ret_rect = ret_rect.get()
print(ret_rect.length)
print(ret_rect.breadth)