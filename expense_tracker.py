print("===== Expense Tracker =====")

expenses = []

for i in range(3):
    expense = float(input("Enter expense amount: "))
    expenses.append(expense)

total = sum(expenses)

print("\n===== Expense Summary =====")
print("Expenses:", expenses)
print("Total Expense:", total)
print("Average Expense:", total / len(expenses))
