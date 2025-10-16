# import os
# import inspect
# print("Current Directory:",os.getcwd())

# functions = inspect.getmembers(os, inspect.isbuiltin)

# print("All function in os module")
# for n, func in functions:
#     print(n)

# . next


#Create a folder inside current directory using python ..... note nnt tak tahu pula kan - cdir(cdrive)(boleh letak nama suka hati)

import os
cdir=os.getcwd()
folder_name=input("Enter Folder Name to create: \t")
folder_path=os.path.join(cdir,folder_name)
if(os.path.exists(folder_path)):
    print("Folder already exist")
else:
    os.makedirs(folder_path,exist_ok=True)
    print(f"{folder_name} created at {folder_path}")


#Rename a folder
# os.rename(folder_name, "renamed_folder")

#Write code to rename a folder
#You will take folderName from user
#If it exist, you will ask a new name and rename it

folder_to_rename = input("Enter name for rename folder: \t")
if os.path.exists(folder_to_rename):
    new_name = input("Enter new name for folder")
    os.rename(folder_to_rename,new_name)
    print(f"Folder rename to {new_name} successfully!")

else:
    print("Renamed successfully changed")


