class DataofClass:
## list contain all students data in it
    all_students = []
    def __init__(self,name,marks):
        self.name = name
        self.marks = marks
        ## put every data into the list by append method
        DataofClass.all_students.append(self)
## to show any object data
 #   def display(self):
 #       print("My name is ", self.name, " and my marks is ", self.marks)

## to calculate average of class marks
    @classmethod
    def average_marks(cls):
        total = 0
        for student in cls.all_students:
            total += student.marks
        average = total / len(cls.all_students)
        return average
    

s1 = DataofClass("Alice", 85)
s2 = DataofClass("Bob", 90)
s3 = DataofClass("Charlie", 95)
s4 = DataofClass("Diana", 88)
print("Average of class makrs is :", DataofClass.average_marks())