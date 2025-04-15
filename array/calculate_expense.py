#expenses = [2200, 2350, 2600, 2130, 2190]
expenses = [10, 20, 30, 40, 50]
months = ["Jan", "Feb", "Mar", "Apr", "May"]

print("Feb over Jan Expense", expenses[1] - expenses[0])
print("Total Expense in Q1", sum(expenses[0:3]))

def check_expense_month(value):
    for(i, expense) in enumerate(expenses):
        if expense == value:
            print("Found expense",value, " in ", months[i])
            return
    print("Expense not found:",value)
    return "Expense not found"
    
check_expense_month(2600)