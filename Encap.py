class Bank_account:
    holder_name=None
    def __init__(self,pin,balance):
        self.__pin=pin
        self._balance=balance
        
    def display_balance(self,pin):
        if self.__pin==pin:
            print("ypur balance is: ", self._balance)
        else:
            print("Invalid pin")
            
    def display_holder_name(self):
        print("Holder name is : " , self.holder_name)
        
    def change_pin(self,old_pin,new_pin):
        if old_pin==self.__pin:
            self.__pin=new_pin
            print("pin changed successfully")
        else:
            print("Invalide old pin ")
            
    def deposite(self,pin,balance):
        if self.__pin==pin:
            self._balance+=balance
            print("money deposite successfully")
        else:
            print("Invalid pin")
            
    def display_pin(self):
        print("pin: ",self.__pin)
        
class joint_account(Bank_account):
    def display_parent_balance(self,pin,balance):
        def __init__(self,pin,balance):
            super().__init__(pin,balance)
        def display_parent_balance(self):
            
            print("Parent balance is: ",self.balance)
            

# account=Bank_account(1234,1000)
# account.holder_name="rahul"
# account.display_holder_name()
# account.display_balance(1234)
#account.change_pin(1234,0000)

# account.deposite(0000,500)
#account.display_pin()

JA = joint_account(1234,0)
JA.display_parent_balance()