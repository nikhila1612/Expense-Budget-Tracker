class Expense:
    def __init__(self,name,category,amount):
        self.name=name
        self.category=category
        self.amount=amount
    
    # To provide a string representation of an object of class 'Expense'
    def __repr__(self):
        return f" {self.name}, {self.category}, ${self.amount:.2f} "   