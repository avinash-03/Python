class Employee:
    company='Google'
    def getSalary(self):
        print(f'Salary is {self.salary}')

    def greet(self):
        print('Good morning sir')

harry=Employee()
harry.salary=1000
harry.getSalary()
harry.greet()