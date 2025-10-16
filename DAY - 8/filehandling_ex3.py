import os
file_paths= r"C:\Users\User\OneDrive\Desktop\AIML\DAY - 8\ourfile/sample.txt"
filepath=os.getcwd()
filename=input("Enter file name to read file: \t")
fullpath=os.path.join(filepath,filename)

if(os.path.exists(fullpath)):
    file=open(fullpath,"a")
    
    content=file.read()
    print("File content as follow")
    file.close()

else:
    print(f"No such file {filename} exist")