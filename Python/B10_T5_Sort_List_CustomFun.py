class Employee:
    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary

    def __repr__(self):
        return f'({self.name},{self.age},{self.salary})'


e1=Employee('karthik', 25, 6000)
e2=Employee('priya', 25, 6000)
e3=Employee('sethu', 25, 6000)

employee = [e1,e2,e3]


def e_sort(emp):
    print("-----")
    print(emp.name)
    return emp.name


s_employee = sorted(employee, key=e_sort)
print(s_employee)