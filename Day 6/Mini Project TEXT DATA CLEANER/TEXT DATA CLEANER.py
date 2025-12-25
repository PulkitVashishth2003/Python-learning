with open ("Day 6/Mini Project TEXT DATA CLEANER/rawdata.txt", "r") as file:
    data = file.read()
    data1 = data.replace(".","\n")
    if "  " in data1:
        data2 = data1.replace("   " or "  ","")
    else:
        data2 = data1

    cleaned_data = data2.lower()

    print(cleaned_data)