class Employee:
    def __init__(self, emp_id, name, age, salary):
        self.emp_id = emp_id
        self.name = name
        self.age = age
        self.salary = salary

    def __str__(self):
        return f'Employee ID: {self.emp_id}, Name: {self.name}, Age: {self.age}, Salary (PM): {self.salary}'

class EmployeeTable:
    def __init__(self):
        self.employees = []

    def add_employee(self, emp_id, name, age, salary):
        employee = Employee(emp_id, name, age, salary)
        self.employees.append(employee)

    def search_by_age(self, age):
        result = []
        for employee in self.employees:
            if employee.age == age:
                result.append(employee)
        return result

    def search_by_name(self, name):
        result = []
        for employee in self.employees:
            if employee.name == name:
                result.append(employee)
        return result

    def search_by_salary(self, operator, salary):
        result = []
        for employee in self.employees:
            if operator == '>':
                if employee.salary > salary:
                    result.append(employee)
            elif operator == '<':
                if employee.salary < salary:
                    result.append(employee)
            elif operator == '>=':
                if employee.salary >= salary:
                    result.append(employee)
            elif operator == '<=':
                if employee.salary <= salary:
                    result.append(employee)
        return result

employee_table = EmployeeTable()
employee_table.add_employee('161E90', 'Raman', 41, 56000)
employee_table.add_employee('161F91', 'Himadri', 38, 67500)
employee_table.add_employee('161F99', 'Jaya', 51, 82100)
employee_table.add_employee('171E20', 'Tejas', 30, 55000)
employee_table.add_employee('171G30', 'Ajay', 45, 44000)

print('Search by Age:')
result = employee_table.search_by_age(41)
for employee in result:
    print(employee)

print('\nSearch by Name:')
result = employee_table.search_by_name('Jaya')
for employee in result:
    print(employee)

print('\nSearch by Salary:')
result = employee_table.search_by_salary('>', 60000)
for employee in result:
    print(employee)