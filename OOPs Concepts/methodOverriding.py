class Fruit:
    def show(self):
        print("My name is:Fruit")
class Mango(Fruit):
    def show(self):
        print("My name is:Mango")
    def charShow(self):
        print("I always grown in summer")
obj=Mango()
obj.show()