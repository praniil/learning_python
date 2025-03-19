class Animal:
    def __init__(self, name):
        self.name = name
    
    def speak(self):
        print(f"{self.name} makes noise")
    
    def __walk(self):
        print(f"{self.name} can walk")
    
    def access_walk(self):
        self.__walk()

    def _prot_method(self):
        print("i am protected method")


class Dog(Animal):
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed

    def bark(self):
        print(f"{self.name} is {self.breed}. It barks!")

class Test():
    def __init__(self):
        pass
    
    def show():
        animal = Animal("Tiger")
        animal._prot_method()
    

def main():
    wild_animal = Animal("Tiger")
    wild_animal.speak()
    rex = Dog("Rex", "Poddle")
    rex.bark()
    rex.speak()
    # rex.__walk()    #will give error no attribute __walk. Because can access private method
    rex.access_walk()
    print("in main")
    wild_animal._prot_method()
    rex._prot_method()
    t1 = Test
    t1.show()
    

if __name__ == "__main__":
    main()        