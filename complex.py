class complex:
    def __init__(self,real,img):
        self.real = real
        self.img = img
    
    def shownumber(self):
        print(self.real,'i +',self.img,"j")
        
    def __add__(self,num2):
        newReal = self.real+ num2.real
        newimg = self.img+ num2.img
        return complex(newReal,newimg)
    
num1 = complex(1,3)
num1.shownumber()

num2 = complex(4,6)
num2.shownumber()

num3 = num1+num2
num3.shownumber()
        