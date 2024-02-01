import sys
import io

from expense import Expense

# Changing the console encoding, to support unicode characters in terminal.
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

def main():
    print(f"💰 Running Expense Tracker!\n")

    expense_file_path ="expenses.csv"

    # Get user input for expense.
    expense = get_user_expense()

    # Write their expense to a file.
    save_expense_to_file(expense,expense_file_path)

    # Read file and brief about expenses.
    summarize_expense(expense_file_path)
 

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


def summarize_expense(expense_file_path):
    print(f"💸 Summarizing User Expense...")
    expenses=[]
    with open(expense_file_path,"r",encoding="utf-8") as f:
        lines = f.readlines()
        for line in lines:
            stripped_line = line.strip()
  

if __name__ =="__main__":
    main()