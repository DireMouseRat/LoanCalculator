import math
import argparse


def pluralize(word, quantity):
    if quantity == 0:
        return str()
    plural = str() if quantity == 1 else 's'
    return f'{quantity} {word}{plural}'


class LoanCalculator:

    def __init__(self):
        self.loan_principal = 0
        self.annuity_payment = 0
        self.differentiated_payment = 0
        self.number_of_payments = 0
        self.nominal_interest_rate = 0
        self.annual_interest_rate = 0
        self.current_repayment_month = 0

    def get_inputs(self, principal, payment, periods, interest):
        self.loan_principal = int(input("Enter the loan principal:\n")) if principal else 0
        self.annuity_payment = float(input("Enter the monthly payment:\n")) if payment else 0
        self.number_of_payments = int(input("Enter the number of periods:\n")) if periods else 0
        self.nominal_interest_rate = float(input("Enter the loan interest:\n")) / 1200 if interest else 0

    def get_principal(self):
        p = self.loan_principal
        a = self.annuity_payment
        d = self.differentiated_payment
        n = self.number_of_payments
        i = self.nominal_interest_rate
        return int(a / ((i * ((1 + i) ** n)) / (((1 + i) ** n) - 1)))

    def get_payment(self):
        p = self.loan_principal
        a = self.annuity_payment
        d = self.differentiated_payment
        n = self.number_of_payments
        i = self.nominal_interest_rate
        return math.ceil(p * (i * ((1 + i) ** n)) / (((1 + i) ** n) - 1))

    def get_periods(self):
        p = self.loan_principal
        a = self.annuity_payment
        d = self.differentiated_payment
        n = self.number_of_payments
        i = self.nominal_interest_rate
        return math.ceil(math.log(a / (a - i * p), 1 + i))

    # def get_interest(self):
    #     p = self.principal
    #     a = self.payment
    #     n = self.periods
    #     i = self.interest
    #     return 0.10 / 12


error_message = "Incorrect parameters"
parser = argparse.ArgumentParser()
parser.add_argument("--type", choices=["annuity", "diff"], required=True)
parser.add_argument("--payment")
parser.add_argument("--principal")
parser.add_argument("--periods")
parser.add_argument("--interest")

args = parser.parse_args()
LC = LoanCalculator()
menu = input("""What do you want to calculate?
type "n" for number of monthly payments,
type "a" for annuity monthly payment amount,
type "p" for loan principal:\n""")

if menu == 'p':
    LC.get_inputs(False, True, True, True)
    print(f"Your loan principal = {LC.get_principal()}!")
elif menu == 'a':
    LC.get_inputs(True, False, True, True)
    print(f"Your monthly payment = {LC.get_payment()}!")
if menu == 'n':
    LC.get_inputs(True, True, False, True)
    periods = LC.get_periods()
    years = pluralize('year', math.floor(periods / 12))
    months = pluralize('month', periods % 12)
    and_str = ' and ' if years and months else ''
    print(f"It will take {years + and_str + months} to repay this loan!")

    # payment = math.ceil(principal / months)
    # if principal % months == 0:
    #     print(f"Your monthly payment = {payment}")
    # else:
    #     last_payment = principal - (months - 1) * payment
    #     print(f"Your monthly payment = {payment} and the last payment = {last_payment}.")
