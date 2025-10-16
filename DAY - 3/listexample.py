# print("List example one")

# my_list = [10, 20, 30, "python",None,True,11.11]

# for item in my_list:
#     print(item)


# my_list = [10, 20, 30, "python",None,True,11,56,"Fauzi"]
# print("Numebr of items in list are:",len(my_list))

# for item in my_list:
#     print(item)


# print("Second Example of list")
# emps=["sam","ghgigi","salehah","kilot","muny","tobito"]

# print("Number of employees",len(emps))
# for emp in emps:
#     print(emp)

# #print(emps) example
# for emp in emps:
#     print(emp,end=" ")

# #sort example  (horizontal)
# #listName.sort()
# emps.sort()
# print("\n list after sorting")
# for e in emps:
#     print(e, end=" ")

# #Reverse example
# #listName.reverse()
# emps.reverse()
# print("\n Employees in decending order")
# for e in emps:
#     print(e,end=" ")


# append, remove, pop insert method
emps=["sam","fary","monbu","kulliwa","nuitf"]
print("Number of employees",len(emps))
for emp in emps:
    print(emp,end=" ")

# append: adds the item at the end of the list
# newEmp=input("\nEnter employee name to add in list")
# emps.append(newEmp)
# print("After adding new employees are:",len(emps))
# for emp in emps:
#     print(emp,end=" ")


#Insert(index,item): This will add item at given index
# newEmp=input("\nEnter employee name to add in list")
# pos=int(input("Enter position where you want to insert inside list:\t"))
# emps.insert(pos,newEmp)
# print("\nAfter adding new employee: Number of employees are:",len(emps))
# for emp in emps:
#     print(emp,end=" ")

# ListName.remove(item): Will remove item from the list.
# only can remove 1 name only
delEmp=input("Employee to remove from the listing:\t")
emps.remove(delEmp)
print(f"Number of employee after deleting {delEmp} in list are:",len(emps))
for emp in emps:
    print(emp,end=" ")


delEmp=input("Employee to remove from the listing:\t")
if delEmp in emps:
    emps.remove(delEmp)
    print(f"Number of employee after deleting {delEmp} in list are:",len(emps))
    for emp in emps:
        print(emp,end=" ")
else:
    print(f" No such item {delEmp} in employee list")

#
# CAN REMOVE MORE THAN 1
# kena cari sendiri nanti

# pop() example
# listName.pop(index): will delete element at given index and return its value
# emps=["sam","fary","monbu","kulliwa","nuitf"]
# print("Number of employees",len(emps))
# for emp in emps:
#     print(emp,end=" ")

# del_index=int(input("Enter index to pop item:\t"))
# print("Pop Result: ",emps.pop(del_index))

# print ("Number of employees after pop() are:",len(emps))
# for emp in emps:
#     print(emp,end=" ")


# find out first and last element from the list
emps=["sam","fary","monbu","kulliwa","nuitf"]
print("Number of employees",len(emps))
for emp in emps:
    print(emp,end=" ")
print("\n First element of employees list is:",emps[0])
print("\n Second element of employees list is:",emps[1])
print("\n Last first element of employees list is:",emps[-1])
print("\n Last second element of employees list is:",emps[-2])
