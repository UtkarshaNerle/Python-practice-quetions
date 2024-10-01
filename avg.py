class student:
    def __init__(self,name,marks):
        self.name = name 
        self.marks = marks
        
    def get_avg(self):
        sum =0
        for i in self.marks:
                sum+=i
        #avg = sum/len(self.marks)
        print('Hello',self.name,'your avg marks is:',sum/3)
            
s1 = student('utkarsha',[89,98,96])      
s1.get_avg()  