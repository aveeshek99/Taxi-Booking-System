#Getter Setter for customer:
class custom():
    def __init__(self,name,address,email,mob,passwo):
        self.name = name
        self.address = address
        self.email = email
        self.mob = mob
        self.passwo = passwo
    def getName(self):
        return self.name
    def getAddress(self):
        return self.address
    def getEmail(self):
        return self.email
    def getMob(self):
        return self.mob
    def getPasswo(self):
        return self.passwo

    def setName(self,name):
        self.name = name
    def setAddress(self,address):
        self.address = address
    def setEmail(self,email):
        self.email = email
    def setMob(self,mob):
        self.mob = mob
    def setPasswo(self,passwo):
        self.passwo = passwo
    def __str__(self):
        return("{},{},{},{},{}".format(self.name,self.address,self.email,self.mob,self.passwo))