import math


def date_type_to_str(date_type, date_count):
    if date_count == 0:
        return str()
    plural = str() if date_count == 1 else 's'
    return f'{date_count} {date_type}{plural}'


class LoanCalculator:

    def __init__(self):
        self.principal = 0
        self.payment = 0
        self.payments_number = 0
        self.nominal_interest_rate = 0

    def get_inputs(self, principal, payment, periods, interest):
        self.principal = int(input("Enter the loan principal:\n")) if principal else 0
        self.payment = float(input("Enter the monthly payment:\n")) if payment else 0
        self.payments_number = int(input("Enter the number of periods:\n")) if periods else 0
        self.nominal_interest_rate = float(input("Enter the loan interest:\n")) / 1200 if interest else 0

    def get_principal(self):
        p = self.principal
        a = self.payment
        n = self.payments_number
        i = self.nominal_interest_rate
        return int(a / ((i * ((1 + i) ** n)) / (((1 + i) ** n) - 1)))

    def get_payment(self):
        p = self.principal
        a = self.payment
        n = self.payments_number
        i = self.nominal_interest_rate
        return math.ceil(p * (i * ((1 + i) ** n)) / (((1 + i) ** n) - 1))

    def get_periods(self):
        p = self.principal
        a = self.payment
        n = self.payments_number
        i = self.nominal_interest_rate
        return math.ceil(math.log(a / (a - i * p), 1 + i))

    # def get_interest(self):
    #     p = self.principal
    #     a = self.payment
    #     n = self.periods
    #     i = self.interest
    #     return 0.10 / 12


LC = LoanCalculator()
menu = input("""What do you want to calculate?
type "n" for number of monthly payments,
type "a" for annuity monthly payment amount,
type "p" for loan principal:\n""")

if menu == 'p':
    LC.get_inputs(False, True, True, True)
    principal = LC.get_principal()
    print(f"Your loan principal = {principal}!")
elif menu == 'a':
    LC.get_inputs(True, False, True, True)
    payment = LC.get_payment()
    print(f"Your monthly payment = {payment}!")
if menu == 'n':
    LC.get_inputs(True, True, False, True)
    periods = LC.get_periods()
    years = date_type_to_str('year', math.floor(periods / 12))
    months = date_type_to_str('month', periods % 12)
    and_str = ' and ' if years and months else ''
    print(f"It will take {years + and_str + months} to repay this loan!")

    # payment = math.ceil(principal / months)
    # if principal % months == 0:
    #     print(f"Your monthly payment = {payment}")
    # else:
    #     last_payment = principal - (months - 1) * payment
    #     print(f"Your monthly payment = {payment} and the last payment = {last_payment}.")
