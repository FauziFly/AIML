import datetime
import inspect
dtclasses = inspect.getmembers(datetime, inspect.isclass)

print("All Classes in datetime module")
for n, func in dtclasses:
    print(n,end="\t")

#date
print("\n ---Current Date today---\n")
print(datetime.date.today())


#time
print("\n ---Current Time Now---\n")
print(datetime.datetime.now().time().replace(microsecond=0))



#time cara ada format seperti am atau pm
cctime=datetime.datetime.now().time().replace(microsecond=0)
formatedtime=datetime.datetime.now().strftime("%I:%M:%S %p")

print("Current time",cctime)
print("Current time",formatedtime)