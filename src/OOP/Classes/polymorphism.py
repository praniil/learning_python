class Car:
    def __init__(self, name):
        self.name = name

    def speed(self):
        print(f"{self.name} it is fast")
        return self.name

class Train:
    def __init__(self, name):
        self.name = name
        
    def speed(self):
        print(f"{self.name} is very fast")
        return self.name
    
class Aeroplane:
    def __init__(self, name):
        self.name = name
        
    def speed(self):
        print(f"{self.name} is very very fast")    
        return self.name

def main():
    c1 = Car("merc")
    t1 = Train("trainnnn")
    a1 = Aeroplane("aero")

    for vehicle in (c1, t1, a1):
        print(vehicle.speed())

if __name__ == "__main__":
    main()
