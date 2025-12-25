class Class:
    def __init__(self,name,role):
        self.name = name
        self.role = role

    def introduce (self):
        print("Hello my name is", self.name,"and i am a ", self.role)

    def update_role(self,new_role):
        self.role = new_role

p1 = Class("Pulkit", "Trainee")
p1.introduce()
p1.update_role("AI Engineer")
print("Updating role...")
p1.introduce()