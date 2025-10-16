# number=1
# print('printing numbers from 1 to 100')
# while(number<=100):
#     print(number,end=" ")
#     number+=1

# #break example
# num=1
# print('print numbers from 1 to 100 those are not divisible by 11')
# while(num<=100):
#     if(num%11==0):
#         break
#     print(num,end="")
#     num+=1

#     #continue example
# num=1
# print('print numbers from 1 to 100 those are not divisible by 11')
# while(num<=100):
#     if(num%11==0):
#         num+=1
#         continue
#     print(num,end="\t")
#     num+=1

# for i in range(1,100):
#     if(i%5==0):
#         continue
#     print(i,end='\t')

# correctPwd='abc324'
# counter=1
# while True:
#     pwd=input('Enter password to start the game')
#     if(correctPwd==pwd):
#         print('welcome,access granted')
#         break
#     else:
#         print('wrong password,try again')
# print('***GAME STARTED!!!')

correctPwd='abc324'
counter=0
while True:
    pwd=input('Enter password to start the game')
    if(correctPwd==pwd):
        print('permission granted')
        print('**game started**')
        break
    else:
        print('wrong password,try again')
        counter+=1
        if(counter>=3):
            print('blocked for further attempt')
            break
