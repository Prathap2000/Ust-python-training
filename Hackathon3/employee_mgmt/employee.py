import uuid

class Employee:
    def __init__(self, name, department, designation, gross_salary, tax_rate=0.1, bonus_rate=0.05):
        self.id = uuid.uuid4()
        self.name = name
        self.department = department
        self.designation = designation
        self.gross_salary = gross_salary
        self.tax_rate = tax_rate
        self.bonus_rate = bonus_rate
        self.net_salary = self.calculate_net_salary()

    def calculate_net_salary(self):
        tax = self.gross_salary * self.tax_rate
        bonus = self.gross_salary * self.bonus_rate
        return self.gross_salary - tax + bonus

    def __str__(self):
        return (f"Employee ID: {self.id}\n"
                f"Name: {self.name}\n"
                f"Department: {self.department}\n"
                f"Designation: {self.designation}\n"
                f"Gross Salary (₹): {self.gross_salary:,.2f}\n"
                f"Tax ({self.tax_rate*100}%): ₹{self.gross_salary * self.tax_rate:,.2f}\n"
                f"Bonus ({self.bonus_rate*100}%): ₹{self.gross_salary * self.bonus_rate:,.2f}\n"
                f"Net Salary (₹): {self.net_salary:,.2f}")

    def to_dict(self):
        return {
            'id': str(self.id),
            'name': self.name,
            'department': self.department,
            'designation': self.designation,
            'gross_salary': self.gross_salary,
            'tax_rate': self.tax_rate,
            'bonus_rate': self.bonus_rate
        }

    @classmethod
    def from_dict(cls, data):
        return cls(
            name=data['name'],
            department=data['department'],
            designation=data['designation'],
            gross_salary=data['gross_salary'],
            tax_rate=data.get('tax_rate', 0.1),
            bonus_rate=data.get('bonus_rate', 0.05)
        )