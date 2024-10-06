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

    def d_product(self):
        return self.price + self.brand
    
product = laptop("")
print(f"Total value of {product.name} in stock: ${product.d_product()}")