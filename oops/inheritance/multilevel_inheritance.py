class Parent:
    def m1(self):
        print("Inside parent m1 method")

class Parent2(Parent):
    def m2(self):
        print("inside parent m2 method")

class Child(Parent2):
    def c(self):
        print("inside child c method")


ch=Child()
ch.c()
ch.m2()
ch.m1()
