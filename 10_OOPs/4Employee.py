class Employee:
    company='Google'
    salary=100

avi=Employee()
rajni= Employee()
Avinash=Employee()
avi.salary=300
rajni.salary=400

print(avi.company)
print(rajni.company)

avi.company='YouTube'

print(avi.company)
print(rajni.company)
print(avi.salary)
print(rajni.salary)
print(Avinash.salary)
print(Avinash.company)

# Below lines throw error AttributeError: 'Employee' object has no attribute 'address'
#print(avi.address)