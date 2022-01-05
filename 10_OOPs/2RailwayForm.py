class RailwayForm:
    formType='RailwayForm'
    def printData(self):
        print(f"Name is {self.name}")
        print(f"Train is {self.train}")
        print(f"Train time is {self.time}")

aviApplication = RailwayForm()
aviApplication.name='Avinash'
aviApplication.train='Hutatma Express'
aviApplication.time='10:00 PM'
aviApplication.printData()