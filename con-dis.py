class User:
    name = ""
    joining_year = 0
    role = ""
    years_on_platform = 0

    def __init__(self, n, y):
        self.name = n
        self.joining_year = y

    def calculate_years(self):
        self.years_on_platform = 2025 - self.joining_year

    def display(self):
        print("Cannot use User class directly.")

class Customer(User):
    def __init__(self, n, y):
        super().__init__(n, y)
        self.role = "Customer"

    def display(self):
        print("Name = " + self.name)
        print("Role = " + self.role)
        print("Years on platform = " + str(self.years_on_platform))
        print("Welcome, valued customer!\n")

class Vendor(User):
    def __init__(self, n, y):
        super().__init__(n, y)
        self.role = "Vendor"

    def display(self):
        print("Name = " + self.name)
        print("Role = " + self.role)
        print("Years on platform = " + str(self.years_on_platform))
        print("Thank you for partnering with us!\n")

cust = Customer("Alice", 2020)
vend = Vendor("Bob", 2018)

cust.calculate_years()
vend.calculate_years()

cust.display()
vend.display()
