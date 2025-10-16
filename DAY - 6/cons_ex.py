# qual maksud (qualification)
class Emp:
    def __init__(self,id,name,qual):
        self.id=id
        self.name=name
        self.qual=qual

    def show_info(self):
        print("ID: ",self.id)
        print("Name: ",self.name)
        print("Qual: ",self.qual)

class Dev(Emp):
    def __init__(self,id,name,qual,domain,project):
        super().__init__(id, name, qual)
        self.domain=domain
        self.project=project
    def show_info(self):
        super().show_info()
        print("Domain: ",self.domain)
        print("Project: ",self.project)


# exercise: Create one emp object with id:1, name= "Sam", qual ="MCA"
emp=Emp(1,"Sam","MCA")
# create one dev object with id=3, name= "Ravi",qual="MTech",Project="eShopping", Domain="dot net"
dev=Dev(3,"Ravi","MTech","e-Shopping","dotnet")
# display dev details
print("Developer details as follows")
dev.show_info()
# display Emp details
emp.show_info()