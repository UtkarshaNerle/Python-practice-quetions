class grand_father:
    def house(self):
        print("i have a house")
        
class father(grand_father):
    def __init__(self):
        print("father's constructor")
    def car(self):
        print("I have a car")
        
# class aunt(grand_father):
#     def jewellery(self):
#         print("i have a jewellery")
        
class son(father):
    def bike(self):
        print(" Ihave a bike")
        super().__init__()
        
son1=son()
son1.bike()
# son1.house()
# son1.jewellery()

# aunt1 = aunt()
# aunt1.house()
# aunt1.jewellery()
        