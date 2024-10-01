class person:
    __name = 'utkatrsha'
    
    def __hello(self):
        print("hello person")
        
    def welcome(self):
        self.__hello()
        print(person.__name  )
p1 = person() 
p1.welcome()
    