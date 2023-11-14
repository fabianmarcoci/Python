class Animal:
    def __init__(self, name, age, habitat):
        self.name = name
        self.age = age
        self.habitat = habitat

    def make_sound(self):
        return "Auauauau"


class Mammal(Animal):
    def __init__(self, name, age, habitat, fur_type):
        super().__init__(name, age, habitat)
        self.fur_type = fur_type

    def give_birth(self):
        return "Giving birth to a live young"


class Bird(Animal):
    def __init__(self, name, age, habitat, wing_span):
        super().__init__(name, age, habitat)
        self.wing_span = wing_span

    def fly(self):
        return "Flying"


class Fish(Animal):
    def __init__(self, name, age, habitat, scale_type):
        super().__init__(name, age, habitat)
        self.scale_type = scale_type

    def swim(self):
        return "Swimming"


class Dog(Mammal):
    def __init__(self, name, age, habitat, fur_type, breed):
        super().__init__(name, age, habitat, fur_type)
        self.breed = breed

    def bark(self):
        return "Woof!"
