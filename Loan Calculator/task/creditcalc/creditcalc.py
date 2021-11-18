import math
import argparse


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
        return [math.ceil((p / n) + i * (p - ((p * (m - 1)) / n))) for m in range(1, n + 1)]

    def get_periods(self):
        p = self.loan_principal
        a = self.annuity_payment
        n = self.number_of_payments
        i = self.nominal_interest_rate
        return math.ceil(math.log(a / (a - i * p), 1 + i))


error_message = "Incorrect parameters"
parser = argparse.ArgumentParser()
parser.add_argument("--type", choices=["annuity", "diff"], required=True)
parser.add_argument("--payment")
parser.add_argument("--principal")
parser.add_argument("--periods")
parser.add_argument("--interest")
parser.error(error_message)


args = parser.parse_args()


LC = LoanCalculator(args.type, args.principal, args.payment, args.periods, args.interest)

print(LC.get_differentiated_payments())

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
