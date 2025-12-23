list = []
while True:
    num = input("Enter a number to add in list or 'done' when finish :")
    if num.lower() == 'done':
        break
    try:
        value = int(num)
        list.append(value)
    except ValueError:
        print("Invalid input. Please enter a valid integer or 'done'.")
if len(list) == 0:
    print("No numbers were entered.")
average = sum(list)/len(list)
print("The average of the list is :", average)