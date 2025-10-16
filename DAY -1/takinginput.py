
# username=input("Enter Use Name")
# age=int(input("Enter age"))
# salary=float(input("Enter Salary"))
# dataKnw=bool(input("Do you know databases?"))
# print("welcome Mr. \\Ms. \t",username)
# print("Your age is ",age)
# print("Salary is: ",salary)
# print("Know the databases? ",dataKnw)


# % Finding Remainder Example
# num1=int(input("First Number:"))
# num2=int(input("Second Number:"))
# result=num1/num2
# print(f"Result after dividing {num1} anby {num2} = /t {result}")

#Multiply Example
# num1=int(input("First Number:"))
# num2=int(input("Second Number:"))
# result=num1*num2
# print(f"Result after multiply {num1} and {num2} = /t {result}")

#Finding Total Example
# num1=int(input("First Number:"))
# num2=int(input("Second Number:"))
# result=num1+num2
# print(f"Result after adding {num1} and {num2} = /t {result}")

#taking more than one input using single line
num1,num2=input("Enter two numbers seperated by space") . split()
result=int(num1)+int(num2)
print(f"numbers entered by you are {num1} and {num2} and addition of numbers {result}")