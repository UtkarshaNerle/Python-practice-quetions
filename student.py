#create student class that takes name & marks of 3 subjects as arguments 
# in constructer then create a method to print the average
class student :
    def __init__(self,name,marks):
        self.name = name
        self.marks=marks
    
    def avg (self):
        sum =0 
        for i in self.marks:
            sum+=i
        print('hey',self.name,'your score is :',sum/3)


s1 = student('utkarsha',[89,90,98])
s1.avg()
