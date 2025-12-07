from scripts.dog import Dog

def main():
    # Create an instance of the Child class
    my_dog = Dog("Buddy", "Golden Retriever")

    # Access methods and attributes from both the child and parent classes
    my_dog.eat()
    my_dog.bark()
    print(f"My dog's name is {my_dog.name}.")


if __name__ == '__main__':
    main()