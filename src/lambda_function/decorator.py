#why is decorator important
# if i want to add the extra funcitonality to the function without actually changing the function 

def decorator_func(original_func):
    def wrapper_func(*args, **kwargs):
        #add some extra funcitonality
        print("add some extra functionality")
        return original_func(*args, **kwargs)
    return wrapper_func

def display():
    print('display function')

decorated_display = decorator_func(display) #wrapper_func assigned to decorated_display
decorated_display()

#another way
@decorator_func
def display1():
    print("i am in dispaly1")

display1()

@decorator_func
def display_with_arg(name:str, age:int):
    print(f"{name} and {age}",)

display_with_arg("Pranil", 22)