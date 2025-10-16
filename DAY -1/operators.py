#Arithmetic operators: +, -, *, / etc

#  price=float(input("Enter Product Price"))
# discount=price*0.10
# disPrice=price-discount
# print(f"Price: {price}\nDiscount: {discount} \nDiscountPrice: {disPrice}")



# Assignment operators: =, +=, -= etc.

# salary=50000.50
# bonus=5000.60
# print(f"Salary {salary} and Bonus {bonus}")
# salary+=bonus
# print("Salary with Bonus",salary)


# salary=50000.50
# tds=salary*10
# print(f"Salary {salary} and TDS {tds}")
# salary-=tds
# print("Salary after tax",salary)



# Comparison operators: ==, >, >=, <, != etc
# if(condition)
#code
#else
#code

# age=int(input("enter your age"))
# if(age>=18):
#     print("you are eligible to cast your vote , you are the future")
# else:
#     print("SORRY BOLEH NAIK LORRY! You are not eligible to cast your vote")
# print("End of program BOSHKURR")

# marks=int(input("Enter marks percentage without '%' sign"))
# if(marks<30) :
#     print("fail in exam loser")
# else:
#     print("Cleared the exam.good job boshkurr")    

# ! means not equal 
# accessCode="abc123"
# accessCode=input("Enter Access Code")
# if(accessCode!="abc123"):
#     print("Invalid Access Code")
# else:
#     print("Hello Fauzi! Welcome to your course")    

# == Means eaqual
# accessCode=input("Enter Access Code:\t")
# if(accessCode=="abc123"):
#     print("Welcome to our courses dear student")
# else:
#     print("Invalid Access Code")



# Logical operators: and, or, not. 

# phyMarks=int(input("Enter marks obtained in Physics"))
# cheMarks=int(input("Enter marks obtained in chemistry"))
# mathMarks=int(input("Enter marks obtained in Mathematic"))

# if(mathMarks>=50) and (phyMarks>=55) and (cheMarks>=60):
#     print("You are eligible to sit in pre exam of MBBS")
# else:
#     print("You have not got the required marks")

mathMarks=int(input("Enter marks obtained in Mathematics :\t"))
gapYear=int(input("Enter year gap if any otherwise zero :\t"))
if((mathMarks<=55) or (gapYear!=0)):
    print("Not eligible for BioTech")
else:
    print("Eligible for BioTech")
name=input("Enter user name")
if(not name):
    print("error!!!")
else:
    print("welcome",name)



# idProof=input("Enter Id proof you have: \t")
# if((idProof=="passport")or(idProof=="dL")or(idProof=="voter id")):
#     print(f"Valid Id {idProof} we accept here")
# else:
#     print("only passport, dL and voter id are accepted as Identitiy Proof")
#     print(f"{idProof}:is not valid ID here") 

