with open ("Day 6/demo.txt", "w") as file:
    file.write("Hello World!!\n")

with open ("demo.txt", "r") as file:
    content = file.read()
    print(content)