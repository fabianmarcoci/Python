from Library import Book, DVD, Magazine
from Shape import Circle
from Shape import Rectangle
from Shape import Triangle
from Account import SavingsAccount
from Account import CheckingAccount
from Vehicle import Car
from Vehicle import Motorcycle
from Vehicle import Truck
from Employee import Manager, Intern
from Employee import Engineer
from Employee import Salesperson
from Animal import Mammal
from Animal import Fish
from Animal import Bird
from Animal import Dog
if __name__ == '__main__':
    circle = Circle("red", 5)
    print("Circle color is:", circle.color)
    print("Circle Area:", circle.calculate_area())
    print("Circle Perimeter:", circle.calculate_perimeter())

    rectangle = Rectangle("blue", 10, 5)
    print("Rectangle color is:", rectangle.color)
    print("Rectangle Area:", rectangle.calculate_area())
    print("Rectangle Perimeter:", rectangle.calculate_perimeter())

    triangle = Triangle("green", 3, 4, 5)
    print("Triangle color is:", triangle.color)
    print("Triangle Area:", triangle.calculate_area())
    print("Triangle Perimeter:", triangle.calculate_perimeter())

    print("------------------------------------")

    savings_account_1 = SavingsAccount("Fabian Marcoci", "12345")
    savings_account_1.deposit(1000)
    print(f"Savings account Balance: {savings_account_1.funds}")
    print(f"Monthly interest: {savings_account_1.calculate_monthly_interest()}")

    savings_account_2 = SavingsAccount("Andrei Andrei", "12345")

    checking_account = CheckingAccount("Fabian Marcoci", "12345")
    checking_account.deposit(500)
    print(f"Checking account Balance: {checking_account.funds}")
    checking_account.calculate_monthly_interest()

    checking_account.withdraw(200)
    print(f"Checking account Balance after withdrawal: {checking_account.funds}")

    print("------------------------------------")

    car = Car("Toyota", "Yaris", 2020, 28, 2000)
    print(f"Car Info: {car.make} {car.model}, Year: {car.year}, Sits: {car.sits}")
    print(f"Car Mileage for 10 gallons: {car.calculate_mileage(10)} miles")
    print(f"Car Towing Status for 1500 lbs: {car.calculate_towing_capacity(1500)}")

    motorcycle = Motorcycle("Harley-Davidson", "Street 750", 2019, 55)
    print(f"Motorcycle Info: {motorcycle.make} {motorcycle.model}, Year: {motorcycle.year}, Sits: {motorcycle.sits}")
    print(f"Motorcycle Mileage for 3 gallons: {motorcycle.calculate_mileage(3)} miles")

    truck = Truck("Ford", "F-150", 2021, 15, 13000)
    print(f"Truck Info: {truck.make} {truck.model}, Year: {truck.year}, Sits: {truck.sits}")
    print(f"Truck Mileage for 15 gallons: {truck.calculate_mileage(15)} miles")
    print(f"Truck Towing Status for 14000 lbs: {truck.calculate_towing_capacity(14000)}")

    print("------------------------------------")

    manager = Manager("Fabian", "123", 9000, "Engineering")
    print(f"{manager.name} manages the {manager.department} department.")

    engineer1 = Engineer("Andrei", "456", 7000, "Software")
    engineer2 = Engineer("Mihai", "789", 6800, "Hardware")
    print(f"{engineer1.name} is a {engineer1.technical_field} engineer.")
    print(f"Number of Software Engineers: {engineer1.how_many_techs_are_in_the_field()}")

    salesperson = Salesperson("Alex", "234", 5000, 0.05)
    print(f"{salesperson.name}'s annual salary: {salesperson.calculate_annual_salary()}")
    print(f"Commission on $20000 sales: {salesperson.calculate_commission(20000)}")
    print(manager.evaluate_employee(engineer1))

    intern = Intern("Razvan", "I456", "Software Development")
    print(intern.learn())

    print("------------------------------------")

    dog = Dog("Happy", 3, "House", "Short fur", "Golden Retriever")
    print(f"{dog.name} says: {dog.bark()}")
    print(f"{dog.name} says: {dog.make_sound()}")

    print("------------------------------------")

    book = Book("1984", "123456789", "George Orwell", 328)
    dvd = DVD("Inception", "987654321", "148 minutes", "PG-13")
    magazine = Magazine("National Geographic", "555555555", "June 2021")

    print(book.display_info())
    print(book.check_out())
    print(book.return_item())

    print(dvd.display_info())
    print(dvd.check_out())

    print(magazine.display_info())
    print(magazine.check_out())