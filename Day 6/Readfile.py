with open ("Day 6/demo.txt", "a") as file:
    file.write("This is a code generated file for testing purposes.\n")

with open("Day 6/demo.txt", "r") as file:
    data = file.read()
    print(data)