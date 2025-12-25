with open("Day 6/demo.txt", "a") as file:
    file.write("25-Dec-2025 : Open file demo.txt")

with open ("Day 6/demo.txt","r") as file:
    content = file.read()
    print(content)