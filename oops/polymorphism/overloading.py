class Calculator:
    def add(self,n1,n2):
        return n1+n2
    
    def add(self,n1,n2,n3):
        return n1+n2+n3
    
    def add(self,n1,n2,n3,n4):
        return n1+n2+n3+n4
    

    # this is method overloading.same method name,different in count of the parameters,it only stotres the recent method that added to this
op=Calculator()
# print(op.add(10,20))   not possible.can make possible with args and kwargs
print(op.add(2,4,5,6))