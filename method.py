class student :
    college_name =  'MRIT College'
    
    def __init__(self,name,marks):
        self.name = name
        self.marks = marks
        
    def welcome(self):
        print("welcome student",self.name)
        
    def get_marks(self):
        return self.marks
    
s1 = student('utkarsha',99)
s1.welcome()
print(s1.get_marks())