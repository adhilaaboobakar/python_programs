# multiple inheritance
# two same methods in different classes called,it should return the method in the order in which inherited class.java does not support multiple inheritance



class P1:
    def m1(self):
        print("inside m1 method")

class P2:
    def m2(self):
        print("inside m2 method")

class Child(P1,P2):
    pass

ch=Child()
ch.m1()
ch.m2()
