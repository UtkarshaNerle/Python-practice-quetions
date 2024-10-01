class car :
    @staticmethod
    def start():
        print("car started..")
        
    @staticmethod
    def stop():
        print("car stopped..")
        
class Toyotocar(car):
    def __init__(self,brand):
        self.brand = brand

class Fortuner(Toyotocar):
    def __init__(self, type):
        self.type = type

car1 = Fortuner('diesel')
print(car1.type)