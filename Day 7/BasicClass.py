class Class:
    def __init__(self,name,role):
        self.name = name
        self.role = role

    def introduce (self):
        print("Hello my name is", self.name,"and i am a ", self.role)

p1 = Class("Pulkit", "Trainee")
p1.introduce()