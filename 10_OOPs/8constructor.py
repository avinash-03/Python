class Employee:
    company = "Google"

    def __init__(self, name, salary, subunit):
        self.name=name
        self.salary=salary
        self.subunit=subunit
        print('Employee is created')

    def getDetails(self):
        print("The employee name is ",self.name)
        print('the salary of the employee is ',self.salary)
        print('the subunit of employee is',self.subunit)



    def getSalary(self, signature):
        print(f"Salary for this employee working in {self.company} is {self.salary}\n{signature}")

    @staticmethod
    def greet():
        print("Good Morning, Sir")

    @staticmethod
    def time():
        print("The time is 9AM in the morning")

harry = Employee('avi',200,'india')
harry.salary = 100000
harry.getSalary("Thanks!") #  Employee.getSalary(harry)
harry.greet() # Employee.greet()
harry.time()

#harry.Employee() # this throw error 3 positional required
harry.getDetails()