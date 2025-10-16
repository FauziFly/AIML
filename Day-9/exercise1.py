#write a function to check a number is odd or even
def check_odd_even(number):
    if(number%2==0):
        print(f"{number} is even")
    else:
        print(f"{number} is odd")

given_number=int(input("Enter Number: \t"))
check_odd_even(given_number)
print('End')