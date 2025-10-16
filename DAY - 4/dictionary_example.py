employee={"id":1,
          "name":"Fauzi",
          "salary":55000.50
         }

# print("Employee details as follows")
# for key, value in employee.items():
#     print(key, "->", value)
# # Adding key in dictionary.
# employee["City"]="Muscat"
# print("\nDictionary after adding city\n")

# for key, value in employee.items():
#     print(key,"->",value)

# del employee["salary"]
# print("\n Employee Details after deleting Salary \n")
# for key, value in employee.items():
#     print(key,"->",value)
employee={"id":1,
          "name":"Fauzi",
          "salary":55000.50
         }
print("All keys from employee")
for k in employee.keys():
    print(k,end="\t")

print("\nAll values from employee \n")
for v in employee.values():
    print(v,end="\t")

print("\n Key :\t value")
for v in employee.items():
    print(k,":",v)

print("Dictionary as follows")
print(employee)
del employee["salary"]
print("After deleting salary")
for k,v in employee.items():
    print(k," : ",v)