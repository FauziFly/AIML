def add(num1,num2):
    return num1+num2

def multi(num1,num2):
    return num1*num2

def avg(num1,num2):
    return(num1+num2)/2

def sub(num1,num2):
    return num1-num2

def div(num1,num2):
    return num1/num2
print("Welcome to our calculator")
while True:
    print("Select operation \n1.Add \n2.Sub \n3.Multi \n4.Division \n5.Average \n6.Exit")
    operation=int(input("Enter your operation choice(1-6):\t"))
    if(operation==6):
        print("Goodbye")
        break
    if((operation>=6) or(operation<=0)):
        print("Wrong operation choice only 1 to 6 are allowed")
    else:
        fnum=float(input("Enter first number:\t"))
        snum=float(input("Enter second number:\t"))
        if(operation==1):
            print(f"Result after adding {fnum},{snum}:\t",add(fnum,snum))
        if(operation==2):
            print(f"Result after subtracting {fnum},{snum}:\t",sub(fnum,snum))
        if(operation==3):
            print(f"Result after multiplying {fnum},{snum}:\t",multi(fnum,snum))
        if(operation==4):
            print(f"Result after dividing {fnum},{snum}:\t",div(fnum,snum))
        if(operation==5):
            print(f"Average of {fnum},{snum}:\t",avg(fnum,snum))
        if((operation>=6) or(operation>=0)):
            print("Wrong operation choice, please choose only 1 to 6")
        break