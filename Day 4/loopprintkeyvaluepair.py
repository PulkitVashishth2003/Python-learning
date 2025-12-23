studentData = {}
stu1 = {101:{'name':'Alice', 'age':'20', 'course':'Physics', 'marks': 90}}
studentData.update(stu1)
stu2 = {102:{'name':'Bob', 'age':'22', 'course':'Chemistry', 'marks': 85}}
studentData.update(stu2)
stu3 = {103:{'name':'Charlie', 'age':'21', 'course':'Mathematics', 'marks': 88}}
stu4 = {104:{'name':'Diana', 'age':'23', 'course':'Biology', 'marks': 92}}
studentData.update(stu3)
studentData.update(stu4)
for key, value in studentData.items():
    print ("key: ", key, " value: ", value)
