class Class:
    def __init__(self,name,role):
        self.name = name
        self.role = role

    def introduce (self):
        print("Hello my name is", self.name,"and i am a ", self.role)

p1 = Class("Pulkit", "Trainee")
p2 = Class("John", "Developer")
p3 = Class("Alice", "Designer")
p4 = Class("Bob", "Manager")
p5 = Class("Eve", "Intern")
p1.introduce()
p2.introduce()
p3.introduce()
p4.introduce()
p5.introduce()