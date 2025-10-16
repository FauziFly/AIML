# print("Sets in python")
# set_one={"laptop","ps5","gameboy","ipad","window","laptop","smartphone"}
# print("Number of items in set_one are:",len(set_one))
# for item in set_one:
#     print(item,end=" ")

# #clear(): remove all the items from set
# set_one.clear()
# print("\n After clear Number of items in set_one are:",len(set_one))
# for item in set_one:
#     print(item,end=" ")
# ------------------------------
# set_one={"laptop","ps5","gameboy","ipad","window","smartphone"}
# print("Number of items in set_one are:",len(set_one))
# for item in set_one:
#     print(item,end=" ")
# #set.remove(item): update the set and removes item from set.
# set_one.remove("ps5")
# print("\n After removing one item from set:",len(set_one))
# for item in set_one:
#     print(item,end=" ")

# Union,intersection,difference
# set_one={100,200,300,500,700,900,150}
# set_two={100,400,700,1000,1300}
# set_three={5000,11500,345}
# union
#s1.union(s2): Returns a new set with all items from sets s1,set2,set3.
# print(f"set_one contains: {len(set_one)} items")
# print(set_one)
# print(f"set_two contains: {len(set_two)} items")
# print(set_two)
# print(f"set_three contains: {len(set_three)} items")
# print(set_three)
# unionset=set_one.union(set_two,set_three)
# print(f"Union of set_one , set_two and set_three contains: {len(unionset)} following items")

# print(unionset)



# # Union,intersection,difference
# set_one={100,200,300,500,700,900,150}
# set_two={100,400,700,1000,1300}

# # union
# #s1.union(s2): Returns set which contains items only in both sets set1 & set3.
# # union
# print(f"set_one contains: {len(set_one)} items")
# print(set_one)
# print(f"set_two contains: {len(set_two)} items")
# print(set_two)
# newest=set_one.intersection(set_two)
# print(f"Union of set_one , set_two and set_three contains: {len(newest)} following items")
# print(newest)



# set_one={100,200,300,500,700,900,150}
# set_two={100,400,700,1000,1300}
# #Difference example
# #s1.union(s2): Returns set which contains items only in those are in set1 but not set2.
# print(f"set_one contains: {len(set_one)} items")
# print(set_one)
# print(f"set_two contains: {len(set_two)} items")
# print(set_two)
# newest=set_one.difference(set_two)
# print(f"Difference of set_one , set_two contains: {len(newest)} following items")
# print(newest)


