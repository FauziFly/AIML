# class Account:
#     def __init__(self,ac_holder,bal):
#         self.ac_holder=ac_holder
#         self.bal=bal

#     def deposit(self,amount):
#         self.bal+=amount
#         print("Balance after deposit",self.bal)

#     def withdraw(self,amount):
#         if(self.bal>=amount):
#             self.bal-=amount
#             print("Balance after withdraw: ",self.bal)
#         else:
#             print("insufficient amount in account")
#             print("Transaction Failed")
#     def show(self):
#         print(f"Account holder name: {self.ac_holder} Account Balance {self.bal}")


# # ac1=Account("sameer",50000)
# # ac2=Account("chang",14000)
# # ac1.show()
# # ac2.show()
# ac1=Account("Sameeer",50000)

# ac1.show()
# wamount=float(input("Enter amount to withdraw"))
# ac1.withdraw(wamount)

# class Account:
#     def __init__(self, balance,ac_holder):
#         self.balance = balance
#         self.ac_holder=ac_holder

#     def get_balance(self):
#         return self.balance
    
# acc = Account(1000, "Sam")
# acc.balance=34000
# print(acc.balance)

# .

class Account:
    def __init__(self,ac_holder,bal):
        self.ac_holder=ac_holder
        self.bal=bal

    def deposit(self,amount):
        self.bal+=amount
        print("Balance after deposit",self.bal)

    def withdraw(self,amount):
        if(self.bal>=amount):
            self.bal-=amount
            print("Balance after withdraw: ",self.bal)
        else:
            print("insufficient amount in account")
            print("Transaction Failed")
    def show(self):
        print(f"Account holder name: {self.ac_holder} Account Balance {self.bal}")


ac=Account("Sam",15000)
ac.show()

# # cara sir (simple)
print("Please choose\n 1.Deposit 2.Withdraw")
op=int(input())

if(op==1):
    damount=float(input("Enter amount to deposit"))
    ac.deposit(damount)
if(op==2):
    damount=float(input("Enter amount to withdraw"))
    ac.withdraw(damount)
if(op==3):
    ac.show()
else:
    print("Wrong choice")
                  

#  cara chatgpt (advance sikit)
# while True:
#     choice = int(input("Enter your choice (1 or 2): "))
    
#     if choice == 1:
#         amt = float(input("Enter amount to deposit: "))
#         ac.deposit(amt)
        
#     elif choice == 2:
#         amt = float(input("Enter amount to withdraw: "))
#         ac.withdraw(amt)
        
#     else:
#         print("Invalid choice! Please choose 1 or 2.")

#     more = input("Do you want to perform another transaction? (y/n): ")
#     if more.lower() != 'y':
#         print("Thank you for banking with us!")
#         break