#Getter Setter for Driver:
class drive():
    def __init__(self,name,email,address,mob,lice,passwo):
        self.name = name
        self.address = address
        self.email = email
        self.mob = mob
        self.lice = lice
        self.passwo = passwo
    def getName(self):
        return self.name
    def getAddress(self):
        return self.address
    def getEmail(self):
        return self.email
    def getMob(self):
        return self.mob
    def getLice(self):
        return self.lice
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
    def setLice(self,lice):
        self.lice = lice
    def setPasswo(self,passwo):
        self.passwo = passwo
    def __str__(self):
        return("{},{},{},{},{}".format(self.name,self.address,self.email,self.mob,self.lice,self.passwo))