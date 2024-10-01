class car :
    @staticmethod
    def start():
        print("car started")
        
    @staticmethod
    def stop():
        print("car stopeed..")
        
class Toyotocar(car):
        def __init__(self,name):
            self.name = name
    
car1 = Toyotocar("fortuner")
print(car1.name)
print(car1.start())
