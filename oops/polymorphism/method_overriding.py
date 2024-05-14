# in method overriding there should be 2 classes,and a relation b/w 2 classes

class Parent:

    def mobile(self):
        print("redmi note 12")

    def vehicle(self):
        print("splender")


class Child(Parent):
    def mobile(self):
        print("Iphone15")


ch=Child()
ch.mobile()
ch.vehicle()