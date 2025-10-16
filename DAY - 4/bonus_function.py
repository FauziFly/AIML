


# Write a function to calculate bonus of given salary
# Function take salary as input and return bonus 10% of salary

#pengiraan secara luar drpd main function ....function kat luar akan return ke dalam main
def calc_bonus(salary):
    return salary*0.10

salary=float(input("Enter your salary to find your bonus "))
print("bonus is: \t",calc_bonus(salary))


#pengiraan secara direct dalam main function
bonus=salary*0.10
print(f"Salary is: {salary} bonus is: \t",bonus)

