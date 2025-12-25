with open ("Day 6/demo.txt", "r") as file:
    content = file.read()

count = 0
for line in content.split("."):
    count += 1

print("Number of lines in the file:", count)
    