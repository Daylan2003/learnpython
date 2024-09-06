class Employee:
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'

    def fullname(self):
        return '{} {}'.format(self.first, self.last)

emp_1 = Employee('Daylan', 'Maharaj', 100000)
emp_2 = Employee('Daylan2', 'Maharaj2', -100000)

print(emp_1.email)
print(emp_2.email)

print(emp_1.fullname())

