class student:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def display(self):
        print(f"student name: {self.name}")
        print(f"student age: {self.age}")

student1 = student("kath", "22")
student1.display()
