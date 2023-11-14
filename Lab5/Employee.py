class Employee:
    def __init__(self, name, employee_id, salary):
        self.name = name
        self.employee_id = employee_id
        self.salary = salary

    def calculate_annual_salary(self):
        return self.salary * 12


class Manager(Employee):
    def __init__(self, name, employee_id, salary, department):
        super().__init__(name, employee_id, salary)
        self.department = department

    def evaluate_employee(self, employee):
        if employee.salary > 5000:
            return f"{employee.name} is performing well in his department."
        else:
            return f"{employee.name} needs improvement in his department."


class Engineer(Employee):
    tech_number = {}

    def __init__(self, name, employee_id, salary, technical_field):
        super().__init__(name, employee_id, salary)
        self.technical_field = technical_field
        if technical_field not in Engineer.tech_number:
            Engineer.tech_number[technical_field] = 0
        Engineer.tech_number[technical_field] += 1

    def how_many_techs_are_in_the_field(self):
        return Engineer.tech_number[self.technical_field]


class Intern(Engineer):
    def __init__(self, name, employee_id, technical_field):
        super().__init__(name, employee_id, 0, technical_field)  # Assuming interns have no salary or a nominal stipend

    def learn(self):
        return f"{self.name} is learning about {self.technical_field}."


class Salesperson(Employee):
    def __init__(self, name, employee_id, salary, commission_rate):
        super().__init__(name, employee_id, salary)
        self.commission_rate = commission_rate

    def calculate_commission(self, sales_amount):
        return sales_amount * self.commission_rate
