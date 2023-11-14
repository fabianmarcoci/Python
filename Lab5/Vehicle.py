class Vehicle:
    def __init__(self, make, model, year, miles_per_gallon, sits):
        self.make = make
        self.model = model
        self.year = year
        self.miles_per_gallon = miles_per_gallon
        self.sits = sits

    def calculate_mileage(self, gallons):
        return self.miles_per_gallon * gallons


class Car(Vehicle):
    def __init__(self, make, model, year, miles_per_gallon, towing_capacity, sits=4):
        super().__init__(make, model, year, miles_per_gallon, sits)
        self.towing_capacity = towing_capacity

    def calculate_towing_capacity(self, load):
        if load > self.towing_capacity:
            return "Overload"
        else:
            return "Safe to tow"


class Motorcycle(Vehicle):
    def __init__(self, make, model, year, miles_per_gallon, sits=2):
        super().__init__(make, model, year, miles_per_gallon, sits)


class Truck(Vehicle):
    def __init__(self, make, model, year, miles_per_gallon, towing_capacity, sits=2):
        super().__init__(make, model, year, miles_per_gallon, sits)
        self.towing_capacity = towing_capacity

    def calculate_towing_capacity(self, load):
        if load > self.towing_capacity:
            return "Overload"
        else:
            return "Safe to tow"
