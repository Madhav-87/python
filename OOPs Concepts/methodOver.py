class Fruit:
    def showSum(self,a,b,c=None):
        self.a=a
        self.b=b
        self.c=c
        if(c):
            print("The sum of 3 numbers are:",self.a+self.b+self.c)
        else:
            print("The sum of 3 numbers are:",self.a+self.b)
obj=Fruit()
obj.showSum(10,20,30)