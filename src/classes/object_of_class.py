import copy
class Animal:   
    def __init__(self, name = "pemerian"):
        self.name = name
        self.list_test = [1, 2, 3, 4]
    

dog = Animal()
print(id(dog))  #id(object) --> returns the permanent memory address for its entire lifetime

dog1 = copy.copy(dog)
dog2 = copy.deepcopy(dog)
dog3 = dog

dog.name = "Husky"
dog.list_test.append(10)

print(f"id of dog: {id(dog)} and id of dog1: {id(dog1)}") ## shallow copy, outer object is copied but inner mutable objects are shared
print(f"name of dog: {dog.name} and name of dog1: {dog1.name}") #string, int, tuple are immutable. so name is different for each object
print(f"lisst of dog: {dog.list_test} and list of dog1: {dog1.list_test}")

print(f"id of dog: {id(dog)} and id of dog2: {id(dog2)}") ## deep copy copies the entire object graph recursively so everyting is independent
print(f"name of dog: {dog.name} and name of dog2: {dog2.name}")
print(f"list of dog: {dog.list_test} and listl of dog2: {dog2.list_test}")

print(f"id of dog: {id(dog)} and id of dog3: {id(dog3)}") ## shallow copy, outer object is copied but inner mutable objects are shared
print(f"name of dog: {dog.name} and name of dog3: {dog3.name}") #string, int, tuple are immutable. so name is different for each object
print(f"lisst of dog: {dog.list_test} and list of dog3: {dog3.list_test}")


#immutablility of int, str, tuple
a = 123
b = a
#both are pointing to same int, they have the same reference
print(id(a))
print(id(b))

#a modified
a = a + 5
print(a)
print(b)
#both are pointing to different int, they have different reference
print(id(a))
print(id(b))


#each instance of a class has its own dictionary
class Student:
    school = "ABFG"     #class attribute
    def __init__(self, name):
        self.name = name

s = Student("Pranil")
s.school = "ABCDEF"
print(s.name)
print(s.school)