class person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


class employee(person):
    def __init__(self, name, age, employee_id, salary):
        super().__init__(name, age)
        self.employee_id = employee_id
        self.salary = salary

    def show_employee_details(self):
        print("Employee ID:", self.employee_id)
        print("Salary:", self.salary)


class manager(employee):
    def __init__(self, name, age, employee_id, salary, department):
        super().__init__(name, age, employee_id, salary)
        self.department = department

    def show_manager_details(self):
        print("name:", self.name)
        print("age:", self.age)
        print("employee ID:", self.employee_id)
        print("salary:", self.salary)
        print("Department:", self.department)


m = manager("abc", 30, 1234, 50000, "HR")
m.show_manager_details()