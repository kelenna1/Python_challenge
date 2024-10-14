class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def student(self):
        return f"Name: {self.name}, Age: {self.age}"
    
    def __del__(self):
        print(f"{self.name} has been deleted")
    
school = Person("John", "22")
print(f"{school.student()}")

del school

class Book:
    def __init__(self, author, title, pages):
        self.author = author
        self.title = title
        self.pages = pages 
    
    def __str__(self):
        return f"{self.author} has a book titles {self.title} with about {self.pages} pages."

    def __repr__(self):
         return f"Book( title = {self.title}, author = {self.author}, pages = {self.pages})"
    
book = Book("Kelenna", "Franchise", 300)
print(repr(book))
           
class Animal:
    def __init__(self,eat,sleep):
        self.eat = eat
        self.sleep = sleep

    def __str__(self):
        return f""