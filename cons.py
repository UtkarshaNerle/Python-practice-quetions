class student:
    def __init__(self):
        pass
    def __init__(self,name,marks):
        self.name =name
        self.marks=marks
        print('adding new student in databaser..')
        
s1 = student('utkarsha',90)
print(s1.name,s1.marks)

s1 = student('utkarsh',98)
print(s1.name,s1.marks)