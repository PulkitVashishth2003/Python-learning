class School:
    def Status(self):
        return "He is in this school"
    
class Classroom(School):
    def Room(self):
        return "He is in this Classroom"
    
class Student(Classroom):

    def __init__(self,name):
        self.name = name


    def Name(self):
       ## below both line do same task 
       ## return "His name is {name}".format(name=name)
        return f"His name is {self.name}"
    
student = Student("Alexiander")
print(student.Name())
print(student.Room())
print(student.Status())