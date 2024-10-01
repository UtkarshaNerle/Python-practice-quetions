class car :
    def __init__(self,type):
        self.type = type 
    
    @staticmethod
    def start():
        print("car started..")
   
    @staticmethod
    def stop():
        print("car stopped..")

class Toyotocar(car):
    def __init__(self,name,type):
        super().__init__(type)
        self.name = name
        super().start()
               
car1 = Toyotocar('prius',"electric")
print(car1.type)
print(car1.name)