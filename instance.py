class student:
    college_name = 'MRIT college'
    name = 'utkarsha'
    
    def __init__(self,name ,marks):
        self.name = name
        self.marks = marks
        print(student.college_name)
        
s1 = student('yash', 98)
print(s1.name,s1. marks) 

print(s1.college_name)