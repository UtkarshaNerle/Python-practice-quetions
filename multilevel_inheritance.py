class Grand_father: # multilevel inheritance
    def house(self):
        print("I have a house")
        
class father(Grand_father):
    def house(self):
        print("I have a house.")
    def car(self):
        print("I have a car")
        
class son(father):
    def bike(self):
        print("I have a bike")
        
son1=son()
son1.bike()
son1.car()
son1.house()