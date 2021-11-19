import math
import argparse
import sys


def pluralize(word, quantity):
    if quantity == 0:
        return ''
    plural = '' if quantity == 1 else 's'
    return f'{quantity} {word}{plural}'


class LoanCalculator:

    def __init__(self, loan_type, principal, payment, periods, interest):
        self.loan_type = loan_type
        self.loan_principal = int(principal) if principal else 0
        self.payment_per_period = float(payment) if payment is not None else 0
        self.number_of_payments = int(periods) if periods else 0
        self.nominal_interest_rate = float(interest) / 1200
        self.overpayment = 0
        self.calculate()

    def set_default_overpayment(self):
        p = self.loan_principal
        a = self.payment_per_period
        n = self.number_of_payments
        self.overpayment = int(a * n - p)
        
    def calculate(self):
        if self.loan_type == 'diff':
            if self.payment_per_period == 0:
                [print(month) for month in self.get_differentiated_payments()]
                print()
        elif self.loan_type == 'annuity':
            if self.payment_per_period == 0:
                print(self.get_annuity_payment())
            elif self.loan_principal == 0:
                print(self.get_annuity_principal())
            elif self.number_of_payments == 0:
                print(self.get_time_to_repay())
        print(self.get_overpayment())

    def get_annuity_principal(self):
        a = self.payment_per_period
        n = self.number_of_payments
        i = self.nominal_interest_rate
        p = int(a / ((i * ((1 + i) ** n)) / (((1 + i) ** n) - 1)))
        self.set_default_overpayment()
        return f"Your loan principal = {p}!"

    def get_annuity_payment(self):
        p = self.loan_principal
        n = self.number_of_payments
        i = self.nominal_interest_rate
        a = math.ceil(p * (i * ((1 + i) ** n)) / (((1 + i) ** n) - 1))
        self.set_default_overpayment()
        return f"Your annuity payment = {a}!"

    def get_differentiated_payments(self):
        p = self.loan_principal
        a = self.payment_per_period
        n = self.number_of_payments
        i = self.nominal_interest_rate
        d = [math.ceil((p / n) + i * (p - ((p * (m - 1)) / n))) for m in range(1, n + 1)]
        self.overpayment = int(sum(d) - p)
        return [f"Month {m + 1}: payment is {d[m]}" for m in range(0, len(d))]

    def get_time_to_repay(self):
        p = self.loan_principal
        a = self.payment_per_period
        i = self.nominal_interest_rate
        self.number_of_payments = math.ceil(math.log(a / (a - i * p), 1 + i))
        self.set_default_overpayment()
        n = self.number_of_payments
        y = pluralize('year', math.floor(n / 12))
        m = pluralize('month', n % 12)
        conjunction = ' and ' if y and m else ''
        return f"It will take {y + conjunction + m} to repay this loan!"

    def get_overpayment(self):
        return f"Overpayment = {self.overpayment}"


error_message = "Incorrect parameters."
parser = argparse.ArgumentParser()
parser.add_argument("--type", choices=["annuity", "diff"])
parser.add_argument("--payment")
parser.add_argument("--principal")
parser.add_argument("--periods")
parser.add_argument("--interest")
args = parser.parse_args()

if args.type != 'annuity' and args.type != 'diff':
    print(error_message)
elif args.type is None or args.interest is None:
    print(error_message)
elif args.type == 'diff' and args.payment:
    print(error_message)
elif len(sys.argv) < 5:
    print(error_message)
elif (args.principal and int(args.principal) < 0)\
        or (args.payment and float(args.payment) < 0)\
        or (args.periods and int(args.periods) < 0)\
        or (args.interest and float(args.interest) < 0):
    print(error_message)
else:
    LoanCalculator(args.type, args.principal, args.payment, args.periods, args.interest)
