
from abc import ABC,abstractmethod
class Car(ABC):

    @abstractmethod
    def __init__(self,name,brand,model):
        pass

    @abstractmethod
    def start(self):
        pass
    
    @abstractmethod
    def accelerate(self):
        pass
    
    @abstractmethod
    def stop(self):
        pass

class Swift(Car):

    def __init__(self, name, brand, model):
        self.name=name
        self.brand=brand
        self.model=model
    
    def start(self):
        print("Swift starts")

    def accelerate(self):
        print("Swift stops")

    def stop(self):
        print("Swift Stops")

    def brake(self):
        print("swift brake")

sw=Swift("swift","Maruthi","sw")
sw.start()
sw.stop()
sw.brake()