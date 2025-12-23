studentData = {}
stu1 = {101:{'name':'Alice', 'age':'20', 'course':'Physics', 'marks': 90}}
studentData.update(stu1)
stu2 = {102:{'name':'Bob', 'age':'22', 'course':'Chemistry', 'marks': 85}}
studentData.update(stu2)
print(studentData)
studentData.pop(101)
print(studentData)
studentData.clear()
print(studentData)