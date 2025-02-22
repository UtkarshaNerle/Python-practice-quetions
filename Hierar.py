class father:
    def surname(self):
        print("surname: kammi")
        
class son(father):
    def name(self):
        print("Name : Rohan")

class daughter(father):
    def name(self):
        print("Name : struti")
        
son1 = son()
daughter1=daughter()

son1.name()
son1.surname()

daughter1.name()
daughter1.surname()
