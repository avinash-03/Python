class Train:
    def __init__(self,name,fare,seats):
        self.name=name
        self.fare=fare
        self.seat=seats

    def getStatus(self):
        print(f"the name of train is : {self.name}")
        print(f"the seats available in the train is: {self.seat}")

    def fairInfo(self):
        print(f"the price of the ticket is : Rs {self.fare}")

    def bookTicket(self,num=1):
        if (self.seat<num and self.seat>0):
            print('please enter less than this ticket number')
        elif(self.seat>0):
            print(f"Your ticket has been booked! Your seat number is {self.seat}")
            self.seat=self.seat-num
        else:
            print("Sorry this train is full! Kindly try Tatkal")

    def cancelTicket(self):
        pass

intercity=Train('intercity express',90,100)
intercity.getStatus()
intercity.fairInfo()
intercity.bookTicket(100)
intercity.getStatus()
intercity.bookTicket()
