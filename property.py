class student:
    def __init__(self,phy,chem,math):
        self.phy = phy
        self.chem = chem 
        self.math = math
    @property
    def percentage(self):
        return str((self.phy+self.chem+self.math)/3)+'%'

stu1 = student(89,98,90)
print(stu1.percentage)

stu1.phy = 95
print(stu1.percentage)
