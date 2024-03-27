#Task 1
class User:
    default_language = "English"

    def __init__(self, name, age, type):
        self.name = name
        self.age = age
        self.type = type

user1 = User("Bear", 20, "Mammal")
print(user1.default_language)
print(user1.name)
print(user1.age)

#Task2
class Book:
    default_discount = 0.1
    max_stock = 100

discount = Book.default_discount

max_stock = Book.max_stock
print(discount)
print(max_stock)

#Task3
class WebServer:
    default_port = 80

WebServer.default_port = 443
print(WebServer.default_port)


#Task4
class Programmer:
    salary = 80000
    monthly_bonus = 1000

    def __init__(self, name, age, address, phone, programming_languages):
        self.name = name
        self.age = age
        self.address = address
        self.phone = phone
        self.programming_languages = programming_languages
        # Assigning class attributes directly
        self.salary = Programmer.salary
        self.monthly_bonus = Programmer.monthly_bonus

class Assistant:
    salary = 40000
    monthly_bonus = 550

    def __init__(self, name, age, address, phone, is_bilingual):
        self.name = name
        self.age = age
        self.address = address
        self.phone = phone
        self.is_bilingual = is_bilingual
        # Assigning class attributes directly
        self.salary = Assistant.salary
        self.monthly_bonus = Assistant.monthly_bonus

def calculate_payroll(employees):
    total = 0
    print("\n== Welcome to our Payroll System ==\n")
    for employee in employees:
        salary = round(employee.salary / 12, 2) + employee.monthly_bonus
        print(employee.name.capitalize() + "'s salary is: $" + str(salary))
        total += salary
    print("The total payroll this month will be: $", total)

jack = Programmer("Jack", 45, "5th Avenue", "555-563-345", ["Python", "Java"])
isabel = Programmer("Isabel", 25, "6th Avenue", "234-245-853", ["Javascript"])
nora = Assistant("Nora", 23, "7th Avenue", "562-577-333", True)

employees = [jack, isabel, nora]

calculate_payroll(employees)
