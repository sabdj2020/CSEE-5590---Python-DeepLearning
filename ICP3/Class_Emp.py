# create class emplyee
class employee:
    emp_count = 0
    salary_total = 0
# create the constructor for this class and give attributes value to objects
    def __init__(self, n, f, s, d):
        self.name = n
        self.family = f
        self.salary = s
        self.department = d
        employee.emp_count = employee.emp_count + 1
        employee.salary_total = employee.salary_total + s
# calculate the average salary
    def avg_salary(self):
        average_salary = self.salary_total / self.emp_count
        print("the average salary is " + str(average_salary))
# method to display the emplyees created
    def display(self):
        print("name:" + self.name, "family_name:" + self.family, "salary:" + str(self.salary),
              "department:" + self.department)

# create class fulltime_employee that inherite from the class emplyee
class fulltime_employee(employee):
    def __init__(self, n, f, s, d):
        employee.__init__(self, n, f, s, d)
#instanciate three objects of type emplyee
    emp1 = employee("Sabrina", "Djeddi", 3000, "Developer")
    emp2 = employee("Nelya", "Aliane", 5000, "Designer")
    emp3 = employee("Ghania", "Salhi", 4000, "Manager")
# display these 3 objects
    emp1.display()
    emp2.display()
    emp3.display()

# instanciate an object that inherite from class emplyee and display it
emp4 = fulltime_employee("Tom", "Jerry", 4000, "Electrical")
emp4.display()
# display the salary
print("The number of emplyees is:" + str(employee.emp_count))
employee.avg_salary(employee)
