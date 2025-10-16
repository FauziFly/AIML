# def add(a,b):
#     total= a+b
#     return total

# result=add(12,15)
# print(result)

# addition = lambda a, b: a + b
# multi=lambda a,b:a*b
# div=lambda a,b:a/b
# avg=lambda a,b:(a+b)/2
# sub=lambda a,b:(a-b)

# num1=int(input("enter 1st number"))
# num2=int(input("enter 2nd number"))

# print("multiplication result: ",multi(num1,num2))
# print("subtraction result: ",sub(num1,num2))


check_odd= lambda n:"Odd number" if n%2==1 else "Even number"
num1=int(input("enter number to check odd or even: \t"))
print(check_odd(num1))
