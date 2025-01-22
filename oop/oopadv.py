class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display(self):
        print(f"Name: {self.name}, Age: {self.age}")

    def update_age(self, new_age):
        self.age = new_age

# Example usage
person = Person("Alice", 30)
person.display()  # Output: Name: Alice, Age: 30

person.update_age(31)
person.display()  # Output: Name: Alice, Age: 31