class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def student(self):
        return f"Name: {self.name}, Age: {self.age}"
    
school = Person("John", "22")
print(f"{school.student()}")

