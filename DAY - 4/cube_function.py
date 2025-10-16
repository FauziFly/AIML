print("Write a function to findout the cube of given number")
#5 : 5*5*5 (e.g. cube of 5 is 5*5*5 means 125)
#5 minutes to do this task

#cara sir
def cube(num):
    return num*num*num
given_number=int(input("Enter number to find out cube of number:|t"))
print(f"Number is: {given_number} cube is",cube(given_number))

#cara lain



#Write a function to calculate bonus of given salary
# Function take salary as input and return bonus 10% of salary

def calc_bonus(salary):
    return salary*0.10

salary=float(input("Enter your salary to find your bonus "))
print(f"Salary is: {salary} bonus is: \t",calc_bonus(salary))
bonus=salary*0.10
print(f"Salary is: {salary} bonus is: \t",bonus)
