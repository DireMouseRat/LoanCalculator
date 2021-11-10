import math


class LoanCalculator:

    def __init__(self):
        self.principal = 0
        self.payment = 0
        self.periods = 0
        self.interest = 0

    def get_inputs(self, principal, period, payment, interest):
        self.payment = int(input("Enter the monthly payment:\n")) if payment else 0
        self.principal = int(input("Enter the loan principal:\n")) if principal else 0
        self.interest = float(input("Enter the loan interest:\n")) if interest else 0
        self.periods = int(input("Enter the number of periods:\n")) if period else 0

    def get_payment(self):
        a = self.payment
        p = self.principal
        i = self.interest
        n = self.periods
        return p * (i * (1 + i) ^ n) / ((1 + i) ^ n - 1)

    def get_principal(self):
        a = self.payment
        p = self.principal
        i = self.interest
        n = self.periods
        return a / ((i * (1 + i) ^ n)/((1 + i) ^ n - 1))

    # def get_interest(self):
    #     a = self.payment
    #     p = self.principal
    #     i = self.interest
    #     n = self.periods
    #     return

    def get_periods(self):
        a = self.payment
        p = self.principal
        i = self.interest
        n = self.periods
        return math.log(1 + i, (a / (a - i * p)))


LC = LoanCalculator()
menu = input("""What do you want to calculate?
type "n" for number of monthly payments,
type "a" for annuity monthly payment amount,
type "p" for loan principal:\n""")

if menu == 'n':
    LC.get_inputs(True, True, False, True)
    temp = LC.get_periods()
    print(f"It will take {temp} months to repay the loan")

elif menu == 'a':
    LC.get_inputs(True, True, False, True)
    temp = LC.get_payment()
    years = ''
    months = ''
    print(f"It will take {years} and {months} to repay this loan!")

elif menu == 'p':
    LC.get_inputs(True, True, False, True)
    temp = LC.get_principal()

    # payment = math.ceil(principal / months)
    # if principal % months == 0:
    #     print(f"Your monthly payment = {payment}")
    # else:
    #     last_payment = principal - (months - 1) * payment
    #     print(f"Your monthly payment = {payment} and the last payment = {last_payment}.")
