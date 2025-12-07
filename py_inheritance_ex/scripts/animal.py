# Parent (Base) Class
class Animal:
    def __init__(self, name):
        self.name = name
        print(f"Animal {self.name} created.")

    def eat(self):
        print(f"{self.name} is eating.")
