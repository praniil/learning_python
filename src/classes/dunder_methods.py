class Shape:
    #works completely fine if __init__ is missing. This means the class will still instantiate perfectly fine, but it wont set up any instance attributes automatically at birth
    def area(self, l, b):
        return l * b
    
s = Shape()
print(s.area(1, 3))

#automatic parent Inheritance
class Parent:
    def __init__(self,name):
        self.name = name

#explicitely initializing the parent class
class Child(Parent):
    def __init__(self, name):
        super().__init__(name)

#automatic parent Inheritance
class Child2(Parent):
    pass

child = Child("CHILD")
child2 = Child2("CHILD2")

print(child.name)
print(child2.name)