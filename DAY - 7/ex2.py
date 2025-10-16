# import random

# print("Random number from 1 to 1000")

# print(random.randint(1,1000))

import random
name=input("Input your name")
luckyNumber=random.randint(1,10)
print(f"Welcome Mr.\Ms {name} Coupon Number: {luckyNumber}")
if(luckyNumber==1):
    print("You have won Proton x50")
elif(luckyNumber==7):
    print("You have won Proton Iphone 15")
elif(luckyNumber==3):
    print("You have won Proton ZUS VOUCHER RM5")
else:
    print("Better luck next time")

# .
# .
# .
# .
# .
# .

import random
def findwinner():
    name=input("Input your name")
    luckyNumber=random.randint(1,10)
    print(f"Welcome Mr.\Ms {name} Coupon Number: {luckyNumber}")
    if(luckyNumber==1):
        print("You have won Proton x50")
    elif(luckyNumber==7):
        print("You have won Proton Iphone 15")
    elif(luckyNumber==3):
        print("You have won Proton ZUS VOUCHER RM5")
    else:
        print("Better luck next time")

