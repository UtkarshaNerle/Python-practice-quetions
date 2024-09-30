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
