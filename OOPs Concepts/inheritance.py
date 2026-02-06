class Fruit:
    def __init__(self):
        self.name="Madhav Bondhare"
        self.age=12
        self.certificate="Rough"
class Mango(Fruit):
    def show(self):
        print("Name is:",self.name)
        print("Age is:",self.age)
        print("Certificate is:",self.certificate)
obj=Mango()
obj.show()