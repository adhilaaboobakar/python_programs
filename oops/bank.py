
class Bank:
    acc_num:int
    name:str
    acc_type:str
    ifsc_code:int
    branch:str
    balance:int

    def create_account(self,acc_num,name,acc_type,ifsc_code,branch,balance):
        self.acc_num=acc_num
        self.name=name
        self.acc_type=acc_type
        self.ifsc_code=ifsc_code
        self.branch=branch
        self.balance=balance

    def deposit(self,amount):
        self.balance=self.balance+amount
        print(f"your {self.acc_num} has been credited with {amount} available balance : {self.balance}")

    def withdraw(self,amount):
        if amount>self.balance:
            print("Insufficient balance")
        else:
            self.balance=self.balance-amount
        print(f"your {self.acc_num} is has been debited with {amount} avl balance is {self.balance}")

    def get_balance(self):
        print("your avl bal is :",self.balance)


person1=Bank()
person1.create_account(79000876,"hari","savings","SBIN00700","painav",0)
person1.deposit(2000)
person1.withdraw(1000)
person1.get_balance()

