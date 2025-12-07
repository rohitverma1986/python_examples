from scripts.animal import Animal
# Child (Derived) Class - inherits from Animal
class Dog(Animal):
    def __init__(self, name, breed):
        # Call the parent class's __init__ method using super()
        super().__init__(name)
        self.breed = breed
        print(f"Dog {self.name} is a {self.breed}.")

    def bark(self):
        print("Woof woof!")