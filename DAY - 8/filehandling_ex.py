# file_paths tu (satu ada r method and satru lagi double slash method)...boleh either one

# method 1
# import os
# file_paths= r"C:\Users\User\OneDrive\Desktop\AIML\DAY - 8\ourfile/sample.txt"
# file_paths= "C:\\Users\\User\\OneDrive\Desktop\AIML\DAY - 8\\ourfile/sample.txt"
# file=open(file_paths,"w")
# content=input("Enter text to write in file: \t")
# file.write(content)
# file.close()

# method 2
# import os
# # file_paths= "C:\\Users\\User\\OneDrive\Desktop\AIML\DAY - 8\\ourfile/sample.txt"
# filepath= "C:\\Users\\User\\OneDrive\Desktop\AIML\DAY - 8\\ourfile"
# filename=input("Enter text to create name: \t")
# fullpath=os.path.join(filepath,filename)
# file=open(fullpath,"w")
# content=input("Enter text to write in file")
# file.write(content)
# print(f"File{filename} create at {fullpath} and content saved in file")
# file.close()

# method 3
import os
file_paths= r"C:\Users\User\OneDrive\Desktop\AIML\DAY - 8\ourfile/sample.txt"
filepath=os.getcwd()
filename=input("Enter file name to create file: \t")
fullpath=os.path.join(filepath,filename)
file=open(fullpath,"w")
content=input("Enter text to write in file")
file.write(content)
print(f"File{filename} create at {fullpath} and content saved in file")
file.close()
