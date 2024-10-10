# class student:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
    
#     def display(self):
#         print(f"student name: {self.name}")
#         print(f"student age: {self.age}")

# student1 = student("kath", "22")
# student1.display()

class laptop:
    def __init__(self, name, price, brand):
        self.name = name
        self.price = price
        self.brand = brand

    def __str__(self):
        return f"the name of the laptop is {self.name} and is priced at {self.price},becuase  it is a {self.brand}"
    
product = laptop("Galaxy", "$1999", "Samsung")
print(product)