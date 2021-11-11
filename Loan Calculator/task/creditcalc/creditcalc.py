import math


class LoanCalculator:

    def __init__(self):
        self.principal = 0
        self.payment = 0
        self.periods = 0
        self.interest = 0

    def get_inputs(self, principal, payment, periods, interest):
        self.principal = int(input("Enter the loan principal:\n")) if principal else 0
        self.payment = float(input("Enter the monthly payment:\n")) if payment else 0
        self.periods = int(input("Enter the number of periods:\n")) if periods else 0
        i = float(input("Enter the loan interest:\n")) / 100 if interest else 0
        self.interest = i / 12

    def get_principal(self):
        p = self.principal
        a = self.payment
        n = self.periods
        i = self.interest
        return int(a / ((i * ((1 + i) ** n)) / (((1 + i) ** n) - 1)))

    def get_payment(self):
        p = self.principal
        a = self.payment
        n = self.periods
        i = self.interest
        return math.ceil(p * (i * ((1 + i) ** n)) / (((1 + i) ** n) - 1))

    def get_periods(self):
        p = self.principal
        a = self.payment
        n = self.periods
        i = self.interest
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
    years_num = str(math.floor(periods / 12))
    months_num = str(periods % 12)
    years_str = 'year' if int(years_num) == 1 else 'years'
    months_str = 'month' if int(months_num) == 1 else 'months'
    result = str()
    if periods < 12:
        result = ' '.join([months_num, months_str])
    elif periods == 12:
        result = "1 year"
    elif periods > 12:
        result = ' '.join([years_num, years_str, 'and', months_num, months_str])

    print(f"It will take {result} to repay this loan!")





    # payment = math.ceil(principal / months)
    # if principal % months == 0:
    #     print(f"Your monthly payment = {payment}")
    # else:
    #     last_payment = principal - (months - 1) * payment
    #     print(f"Your monthly payment = {payment} and the last payment = {last_payment}.")
