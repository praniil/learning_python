class Animal:
    legs = 4
    speak = "noise" 
    def __init__(self, name):
        self.name = name


class Dog(Animal):
    def __init__(self, name):
        super().__init__(name)
    speak = "bark"


dog = Dog("tom")
#while searching dog.speak varaible. First the dog.__dict__ is searched, if not found Dog class i.e. Dog.__dict__ searched, if not found ParentClass.__dict__ searched and so on
print(dog.speak)


class Person:
    species = "Human"

    def __init__(self):
        self.name = "Pranil"

p = Person()
print(p.__dict__)
print(p.name)
print(Person.__dict__)
print(p.species) #for p.species, it checks first the dict of instance p and then the dict of class Person