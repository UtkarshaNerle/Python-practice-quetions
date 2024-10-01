class order:
    def __init__(self,item,price):
        self.item = item
        self.price = price
    
    def __gt__(self,ord2):
        return self.price > ord2.price
    
odr1 = order("chips",20)
odr2 = order("tea",15)
    
print(odr1>odr2)