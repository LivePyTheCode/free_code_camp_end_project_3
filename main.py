
class Category:
    def __init__(self, name):
        self.name = name
        self.ledger = []
        self.balance = 0.0

    def deposit(self, amount, description=""):
        self.ledger.append({"amount": amount, "description": description})
        self.balance += amount

    def withdraw(self, amount, description=""):
        if self.check_funds(amount):
            self.ledger.append({"amount": -amount, "description": description})
            self.balance -= amount
            return True
        return False

    def get_balance(self):
        return self.balance

    def transfer(self, amount, category):
        if self.check_funds(amount):
            self.withdraw(amount, f"Transfer to {category.name}")
            category.deposit(amount, f"Transfer from {self.name}")
            return True
        return False

    def check_funds(self, amount):
        return self.balance >= amount

    def __repr__(self):
        title = self.name.center(30, "*") + "\n"
        ledger = ""
        for item in self.ledger:
            line_description = item["description"][:23].ljust(23)
            line_amount = "{:.2f}".format(item["amount"])[:7].rjust(7)
            ledger += f"{line_description}{line_amount}\n"
        total = f"Total: {self.balance:.2f}"
        return title + ledger + total


def create_spend_chart(categories):
    total_spent = [sum(item['amount'] for item in category.ledger if item['amount'] < 0) for category in categories]

    total_spending = sum(total_spent)

    spending_percentages = [(spent / total_spending) * 100 for spent in total_spent]

    chart = "Percentage spent by category\n"
    for i in range(100, -1, -10):
        chart += f"{i:3d}| "
        for percent in spending_percentages:
            chart += "o  " if percent >= i else "   "
        chart += "\n"

    chart += "    " + "-" * (3 * len(categories) + 1) + "\n"


    max_name_length = max(len(category.name) for category in categories)

    formatted_names = [category.name.ljust(max_name_length) for category in categories]

    for i in range(max_name_length):
        chart += "     "
        for name in formatted_names:
            if i < len(name):
                chart += name[i] + "  "
            else:
                chart += "   "
        if i != max_name_length - 1:
            chart += "\n"

    return chart.rstrip("\n")


food = Category("Food")
food.deposit(1000, "initial deposit")
food.withdraw(10.15, "groceries")
food.withdraw(15.89, "restaurant and more food for dessert")

clothing = Category("Clothing")
food.transfer(50, clothing)

categories = [food, clothing]
print(create_spend_chart(categories))

print(food)
print(clothing)
print(Category)
