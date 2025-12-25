with open ("Day 6/demo.txt","a") as file:
    file.write("This is a line written in second code to check.")

with open ("Day 6/demo.txt","r") as file:
    data = file.readlines()
    print(data)