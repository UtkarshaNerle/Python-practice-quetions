class father: #single Inheritance
    def surname(self):
        print("surname : kammi")

class mother:
    def eye_color(self):
        print("eye color : blue")
        
class son(father,mother):
    def name(self):
        print("name : rohan")
son1=son()
son1.name()
son1.surname()
son1.eye_color()