class Employee:
    def __init__(self, first, last, pay):
        self.first = first  # emp_1.first
        self.last = last  # emp_1.last
        self.pay = pay  # emp_1.pay
        self.email = self.first + self.last + "@company.com"  # emp_1.email

    def fullname(self):
        return "{} {}".format(self.first, self.last)
        # print('{} {}'.format(emp_1.first, emp_1.last))
        # print('{} {}'.format(emp_2.first, emp_2.last))


emp_1 = Employee("Corey", "Schafer", 50000)
emp_2 = Employee("Test", "User", 60000)


print(emp_1.fullname())
print(emp_2.fullname())
print(emp_1.fullname)
print(emp_2.fullname)
