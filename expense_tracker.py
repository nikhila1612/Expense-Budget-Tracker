import calendar
import datetime
import sys
import io

from expense import Expense

# Changing the console encoding, to support unicode characters in terminal.
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

def main():
    print(f"💰 Running Expense & Budget Tracker!\n")

    expense_file_path ="expenses.csv"
    budget = float(input('Enter your budget: $'))

    # Get user input for expense.
    expense = get_user_expense()

    # Write their expense to a file.
    save_expense_to_file(expense,expense_file_path)

    # Read file and brief about expenses.
    summarize_expense(expense_file_path,budget)
 

def get_user_expense():
    print(f"💸 Getting User Expense...\n")
    expense_name = input("Enter the name of the expense: ")
    expense_amount = float(input("Enter expense amount: $"))
    expense_categories = [ 
        "🍞 Food",
        "🏡 Home",
        "💼 Work",
        "🎊 Fun",
        "🚗 Travel",        
        "✨ Miscellaneous"
    ]

    while True:
        print(f"Select a category: ")
        # Display's the categories available.
        for i,category_name in enumerate(expense_categories):
            print(f"  {i+1}. {category_name}")
        
        # Range of the categories
        value_range =f"[1-{len(expense_categories)}]"

        # Exception handling, in case anything other than an integer is typed by the user.
        try:
            selected_index = int(input(f"Enter a category number {value_range}: "))-1
            # Checks if the user has entered an integer within the range.
            if selected_index in range(len(expense_categories)):
                # Stores the category choosen by the user in the selected_category variable.
                selected_category=expense_categories[selected_index]
                # Object of the class Expense is created and values are assigned to the attributes of the 'Expense' class
                new_expense = Expense(name=expense_name,category=selected_category,amount=expense_amount)
                return new_expense           

        except Exception:
            print(f"Invalid category. Please try again!")
        break
    


def save_expense_to_file(expense:Expense,expense_file_path):
    print(f"\n💸 Saving User Expense: {expense} to {expense_file_path}")
    # It opens the file specified by 'expense_file_path' in append mode("a").
    # The file opened with the 'utf-8' encoding, which supports a wide range of characters, including emojis.
    # The 'with' statement is used to ensure that the file is properly closed after writing.
    with open(expense_file_path, "a",encoding="utf-8") as f:
        # This line writes a formatted string to the file.
        f.write(f"{expense.name}, {expense.amount}, {expense.category}\n")


def summarize_expense(expense_file_path,budget):
    print(f"💸 Summarizing User Expense...")
    expenses=[]
  
    # Open the expense csv file in read mode with utf-8 encoding
    with open(expense_file_path,"r",encoding="utf-8") as f:
        # Read all lines from the file. All content is stored as a list. 
        lines = f.readlines()
        # Iterate through each line in the file.
        for line in lines:
            # Remove whitespaces from the line using strip() method.
            # Split the line into components (name, amount, category ) using split by comma 
            expense_name, expense_amount, expense_category =line.strip().split(",")
            # Create an object of class 'Expense' and append it to the end of the list.
            line_expense = Expense(name=expense_name, category=expense_category,amount=float(expense_amount))
            expenses.append(line_expense)
    

    # Initialize a dictionary to store total expenses by category
    amount_by_category = {}
    # Iterate through each object of the 'Expense' class in the list 'expenses'
    for expense in expenses:
        # Use the catergory as key
        key = expense.category
        # Check if the category already exists in the dictionary.
        if key in amount_by_category:
            # If exists add the expense amount to the existing total.
            amount_by_category[key] += expense.amount
        else:
            # If not exists, create a new entry in the dictionary
            amount_by_category[key] = expense.amount

    print("Expenses By Category 📈:")
    for key,amount in amount_by_category.items():
        # Print each category and the total amount spend in that category
        print(f"  {key}: ${amount:.2f}")

    # Calculate the total amount spent by summing up the amount attribute of each object of "Expense" class in the expense list.
    total_spent = sum([x.amount for x in expenses])
    print(f"\n💵 Total Spent: ${total_spent:.2f} ")

    # Remaining Budget
    remaining_budget = budget - total_spent
    # Check if the remaining budget is negative(indicating the user has exceeded their budget)
    if remaining_budget<0:
        print(f"You've gone over your budget!!!")
        print(f"📝 Budget Remaining: $0")
    else:
        print(f"📝 Budget Remaining: ${remaining_budget}\n")
  
    # Get the current date
    now =datetime.datetime.now()
    # Get the number of days in the current month
    days_in_month =calendar.monthrange(now.year, now.month)[1]
    # Calculate the remaining number of days in the current month
    remaining_days =days_in_month -now.day
    # Budget Per Day
    daily_budget=remaining_budget/remaining_days
    print(f"🎯 Budget Per Day: ${daily_budget:.2f}")
    

    # Ask the user if they want to clean the expense file(removing all the existing content)
    clean_expense_file = input("Do you want to clean the expense file? (yes/no): ").lower()
    # Check if the user wants to clean the expense file   
    if clean_expense_file == "yes":
        with open(expense_file_path, "w"):
            pass
        print(f"\n🧹 Expense file cleaned!")



# Check if the script is being run as the main program
if __name__ =="__main__":
    # If the script is the main program, execute the following block
    main()