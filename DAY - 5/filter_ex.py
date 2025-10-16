# numbers = [10, 25, 30, 40, 2,1]

# print("\nOriginal List")
# for num in numbers:
#     print(num,end=" ")

# even_numbers= list(filter(lambda x: x%2==0, numbers))

# print("\nEven number from list as follows\n")
# for num in even_numbers:
#     print(num, end=" ")


# odd_numbers= list(filter(lambda x: x%2, numbers))

# print("\nOdd number from list as follows\n")
# for num in odd_numbers:
#     print(num, end=" ")



#write code using filter to find out all number less than 5
#from the list.
#you have following list:
# our_list=[4,2,5,6,7,3,1,10]

# our_numbers= list(filter(lambda x: x<5, our_list))

# print("Original list")
# for num in our_list:
#     print(num, end=" ")

# print("\n New list as follows\n")
# for num in our_numbers:
#     print(num, end=" ")
# Filter example for dictionary.
students_marks={"Sam" :60,
                "raj" :55,
                "yom" :35,
                "gum" :45,
                "caron" :34,
                "waty" :24
                }
print("All students")
print(students_marks)
pass_students=dict(filter(lambda i:i[1]>50, students_marks.items()))
print("Pass students")
print(pass_students)
#.
print("All students")
for k,v in students_marks.items():
    print(f"Name: {k} -> Marks (v)")

pass_students=dict(filter(lambda i:i[1]>50, students_marks.items()))

print("Pass students")
for k,v in pass_students.items():
    print(f"Name: {k} -> Marks {v}")

#.ascending order
for k,v in students_marks.items():
    print(f"Name: {k} -> Marks {v}")

sort_pass_students=dict(pass_students.items(), key=lambda x: x[1])
print("Ascending Order")

for k,v in sort_pass_students.items():
    print(f"Name: {k} -> Marks {v}")
# Descending order
sort_pass_students_desc=dict(sorted(pass_students.items(), key=lambda x: x[1],reverse=True))

print("Descending Order")
for k,v in sort_pass_students_desc.items():
    print(f"Name: {k} -> Marks {v}")
# tak dapat sbb tak jadi descending ...nnt tanye chatgpt





    
    