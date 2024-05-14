

class Book:
    name:str
    author:str
    pages:int
    price:int

    def __init__(self,name,author,pages,price):
        # initializing instance variables
        self.name=name
        self.author=author
        self.pages=pages
        self.price=price

    def display_book(self):
        print(self.name,self.author)

    def __str__(self):
        return self.name

obj=Book("randamoozham","mt",240,650) #constructor invokes when creating obj.
# obj.display_book()
print(obj)