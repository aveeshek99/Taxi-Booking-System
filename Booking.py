#Getter Setter for Booking Trip:
class Book():
    def __init__(self,pickup,dropoff,date,payment):
        self.pickup = pickup
        self.dropoff = dropoff
        self.date = date
        self.payment = payment
    def getPickup(self):
        return self.pickup
    def getDropoff(self):
        return self.dropoff
    def getDate(self):
        return self.date
    def getPayment(self):
        return self.payment

    def setPickup(self,pickup):
        self.pickup = pickup
    def setDropoff(self,dropoff):
        self.dropoff = dropoff
    def setDate(self,date):
        self.date = date
    def setPayment(self,payment):
        self.payment = payment
    def __str__(self):
        return("{},{},{},{}".format(self.pickup,self.dropoff,self.date,self.payment))