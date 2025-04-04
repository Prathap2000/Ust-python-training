class bankAccount(object):
    def __init__(self,acc_holder,balance=0):
        self.acc_holder=acc_holder
        self.balance=balance
    def deposit(self,amount):
        self.balance+=amount
        print(f"Deposited INR {amount} \nCurrent Balance INR {self.balance}")

    def withdraw(self,amount):
        if amount > self.balance:
            print("Low Balance")
        else:
            self.balance-=amount
            print(f"Debited INR {amount} \nCurrent Balance INR {self.balance}")
    def set_interest_rate(cls,new_rate): #the slef for single unite ,the cls is used to convert it in to the class methos
        cls.set_interest_rate=new_rate
        print(f"Updated rate to {cls.set_interest_rate} pct")
    set_interest_rate=classmethod(set_interest_rate)
    def validate_acc_num(account_number):
        return (len(str(account_number))==12 and str(account_number).isdigit)
    validate_acc_num=staticmethod(validate_acc_num)

if __name__ in "__main__":
    ac=bankAccount("prathap",500)
    if (bankAccount.validate_acc_num('123456789123')):
        ac.deposit(2000)
        ac.withdraw(200)
        bankAccount.set_interest_rate(6)


