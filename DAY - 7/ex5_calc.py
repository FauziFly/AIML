# kita dah ada function dekat file calc.py ....so boleh guna mana2 file lain...senang sikit
# contoh untuk darab ....multi

import calc
import ex2

first_num=float(input("Enter first number: "))
second_num=float(input("Enter second number: "))


print(f"Total of {first_num} ,{second_num} =\t"
     ,calc.add(first_num,second_num))
ex2.findwinner()
