contactlist= []
choice = 0
while True:
    choice = int(input("1. Add Contact\n2. View Contacts\n3. Search Contact\n4. Delete Contact\n5. Exit\nEnter your choice: "))
    if choice == 1:
        name = input("Enter Name:")
        phone = input("Enter Phone Number:")
        if len(phone) != 10 or not phone.isnumeric():
            print("Invalid phone number. Please enter a 10-digit numeric phone number.")
            continue
        else:
            contactlist.append({'name': name, 'phone': phone})
            print("Contact added successfully.")
    elif choice == 2:
        if contactlist:
            for contact in contactlist:
                print(contact['name'], contact['phone'])
        else:
            print("No contacts available.")
    elif choice == 3:
        search_name = input("Enter the name to search:")
        key = 0
        for contact in contactlist:
            if contact['name'].lower() == search_name.lower():
                print("Contact Found", contact)
                key = 1
                break
        if key == 0:
            print("Contact not found.")
    elif choice == 4:
        del_name = input("Enter the name to delete:")
        key = 0
        for i in range(len(contactlist)):
            if contactlist[i]['name'].lower() == del_name.lower():
                contactlist.pop(i)
                print("Contact Deleted")
                key = 1
                break
        if key == 0:
            print("Contact not found.")
    elif choice == 5:
        break
    else:
        print("Invalid choice. Please try again.")
