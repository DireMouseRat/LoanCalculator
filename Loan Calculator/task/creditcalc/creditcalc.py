import math
import argparse
import sys


def pluralize(word, quantity):
    if quantity == 0:
        return str()
    plural = str() if quantity == 1 else 's'
    return f'{quantity} {word}{plural}'


class LoanCalculator:

    def __init__(self, loan_type, principal, payment, periods, interest):
        self.loan_type = loan_type
        self.loan_principal = int(principal)
        self.annuity_payment = float(payment) if payment is not None else 0
        self.number_of_payments = int(periods)
        self.nominal_interest_rate = float(interest) / 1200
        self.overpayment = 0

    def get_principal(self):
        p = self.loan_principal
        a = self.annuity_payment
        n = self.number_of_payments
        i = self.nominal_interest_rate
        return int(a / ((i * ((1 + i) ** n)) / (((1 + i) ** n) - 1)))

    def get_payment(self):
        p = self.loan_principal
        a = self.annuity_payment
        n = self.number_of_payments
        i = self.nominal_interest_rate
        return math.ceil(p * (i * ((1 + i) ** n)) / (((1 + i) ** n) - 1))

    def get_differentiated_payments(self):
        p = self.loan_principal
        a = self.annuity_payment
        n = self.number_of_payments
        i = self.nominal_interest_rate

        diffs = [math.ceil((p / n) + i * (p - ((p * (m - 1)) / n))) for m in range(1, n + 1)]
        self.overpayment = sum(diffs) - p
        s, m = '', 0
        for d in diffs:
            m += 1
            s += f"Month {m}: payment is {str(d)}\n"
        return s

    def get_periods(self):
        p = self.loan_principal
        a = self.annuity_payment
        n = self.number_of_payments
        i = self.nominal_interest_rate
        return math.ceil(math.log(a / (a - i * p), 1 + i))

    def get_overpayment(self):
        return f"Overpayment = {self.overpayment}"


error_message = "Incorrect parameters"
parser = argparse.ArgumentParser()
parser.add_argument("--type", choices=["annuity", "diff"])
parser.add_argument("--payment")
parser.add_argument("--principal")
parser.add_argument("--periods")
parser.add_argument("--interest")
args = parser.parse_args()

if args.type != 'annuity' and args.type != 'diff':
    print("Missing type of annuity or diff")
elif args.type is None or args.interest is None:
    print("args.type is None or args.interest is None")
elif args.type == 'diff' and args.payment:
    print("args.type == 'diff' and args.payment has a value")
elif len(sys.argv) < 5:  # The script path is an additional argument counted
    print("Less than 4 arguments")
elif (args.principal and int(args.principal) < 0)\
        or (args.payment and float(args.payment) < 0)\
        or (args.periods and int(args.periods) < 0)\
        or (args.interest and float(args.interest) < 0):
    print("Negative value")

LC = LoanCalculator(args.type, args.principal, args.payment, args.periods, args.interest)

if args.type == 'diff':
    if args.payment is None:
        print(LC.get_differentiated_payments())
        print(LC.get_overpayment())
    pass
else:  # default to Annuity
    pass

# Calculate Differentiated Payments and Overpayment
# --type=diff --principal=1000000 --periods=10 --interest=10
# --type=diff --principal=500000 --periods=8 --interest=7.8

# Calculate Annuity Payment and Overpayment
# --type=annuity --principal=1000000 --periods=60 --interest=10

# Calculate Annuity Principal and Overpayment
# --type=annuity --payment=8722 --periods=120 --interest=5.6

# Calculate Time and Overpayment
# --type=annuity --principal=500000 --payment=23000 --interest=7.8

# if menu == 'p':
#     LC.get_inputs(False, True, True, True)
#     print(f"Your loan principal = {LC.get_principal()}!")
# elif menu == 'a':
#     LC.get_inputs(True, False, True, True)
#     print(f"Your monthly payment = {LC.get_payment()}!")
# if menu == 'n':
#     LC.get_inputs(True, True, False, True)
#     periods = LC.get_periods()
#     years = pluralize('year', math.floor(periods / 12))
#     months = pluralize('month', periods % 12)
#     and_str = ' and ' if years and months else ''
#     print(f"It will take {years + and_str + months} to repay this loan!")

    # payment = math.ceil(principal / months)
    # if principal % months == 0:
    #     print(f"Your monthly payment = {payment}")
    # else:
    #     last_payment = principal - (months - 1) * payment
    #     print(f"Your monthly payment = {payment} and the last payment = {last_payment}.")
