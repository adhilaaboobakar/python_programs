class Shape:
    name:str

    def __init__(self,name):
        self.name=name

    def __str__(self):
        return self.name
    
class Rectangle(Shape):
    l=int
    b=int

    def __init__(self,name,l,b):
        super().__init__(name)
        self.l=l
        self.b=b

    def area(self):
        result=self.l*self.b
        print(result)

class Circle(Shape):
    r=int

    def __init__(self,name,r):
        super().__init__(name)
        self.r=r

    def area(self):
        result=3.14*self.r**2
        print(result)


rec_obj=Rectangle("rectangle",10,6)
rec_obj.area()
print(rec_obj)
cir_obj=Circle("circle",5)
cir_obj.area()