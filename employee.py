class employee:
    def __init__(self,role,dept,salary,loc):
        self.role = role
        self.dept = dept
        self.salary = salary
        self.loc = loc
                
    def showdetails(self):
        print('role = ',self.role)
        print('dept = ',self.dept)
        print('salary = ',self.salary)
        print('loc = ',self.loc)
        
class engineer(employee):
    def __init__(self,name,age):
        self.name = name
        self.age = age
        super().__init__('engineer','IT',4000000,'blr')
        
engg1 = engineer('utkarsha',20)
engg1.showdetails()