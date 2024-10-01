class person:
    name = 'utkarsha'
   
    # def changeName(self,name):
    #     person.name = name
    
    @classmethod
    def changeName(cls,name):
        cls.name = name    
        
p1 = person()
p1.changeName("rahul")
print(p1.name)
print(person.name)

