class Student:
    def __init__(self, name, age, grade):
        self.name = name  # Initialize the 'name' attribute
        self.age = age    # Initialize the 'age' attribute
        self.grade = grade  # Initialize the 'grade' attribute

    def __str__(self):
        return f"Student Name: {self.name}, Age: {self.age}, Grade: {self.grade}"

# Example Usage
student1 = Student("Alice", 20, "A")

# Accessing attributes
print(student1.name)  # Output: Alice
print(student1.grade) # Output: A

# Using the __str__ method
print(student1)  

