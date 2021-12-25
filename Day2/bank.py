from itertools import count

accounts = {}

class Account:

    count = count(start=1)

    def __init__(self,name,balance,pin):
        self.ac_no = next(self.count)
        self.name = name 
        self.balance = balance 
        self.pin = pin
        # storing object in dictionary
        accounts[self.ac_no] = self
        print(f"Dear {self.name}, Your Account has been created with Rs. {self.balance}.\n Also Your Account No. is {self.ac_no} and your pin is {self.pin}")

    def change_pin(new_pin,old_pin):
        if old_pin == self.pin:
            self.pin = new_pin
        else:
            print("Your old pin is incorrect!!") 

    def __str__(self):
        return f"Account No: {self.ac_no}\nName: {self.name}"

    def transfer(self,pin,receiver_name,receiver_acc_no,amount):
        if pin == self.pin:
            #{key:value} dct.get(key)=> if key exists: value else None
            if accounts.get(receiver_acc_no) != None: 
                if receiver_acc_no != self.ac_no:
                    if amount <= self.balance-100:
                        receiver = accounts.get(receiver_acc_no)
                        if receiver.name == receiver_name:
                            # updating sender's balance
                            self.balance = self.balance - amount
                            # updating receiver's balance
                            receiver.balance = receiver.balance + amount 
                            print(f"Your transfer was successful. Your new balance is Rs.{self.balance}")
                        else:
                            print("Sorry receiver's name is incorrect")
                    else:
                        print("Your balance is insufficient")
                else:
                    print("Sorry you can't transfer to yourself")
            else:
                print("Sorry receiver account doesn't exist")
        else:
            print("Your pin is incorrect!! Please try again.")

myAcc = Account(name="JuJu",balance=3000,pin=123)
yourAcc = Account(name="Lucy",balance=9000,pin=362)
yourAcc.transfer(pin=362, receiver_name="JuJu", receiver_acc_no=2, amount=1000)
print(myAcc.balance)

# Assignment: Put a validation to check own account and print("You can't transfer to self.")