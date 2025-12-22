rent = int(input("Enter monthy Rent Expense : ₹ "))
food = int(input("\nEnter monthly Food Expense : ₹ "))
travel = int(input("\nEnter travel Expense : ₹ "))
misc = int(input("\nEnter all your misllenous Expense : ₹ "))

totalExpense = rent+food+travel+misc
averageDayExpense = totalExpense / 30
averageWeeklyExpense = totalExpense / 4

print("\n\nYour total Expense is : ₹ ", totalExpense)
print("\nYour Average Day Expense is : ₹ ",averageDayExpense)
print("\nYour Average Weekly Expense is : ₹ ",averageWeeklyExpense)