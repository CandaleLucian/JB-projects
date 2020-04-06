from math import ceil, floor, log
import argparse

parser = argparse.ArgumentParser(
    description="my variables"
)

parser.add_argument("--type", help="the credit principal", type=str)
parser.add_argument("--principal", help="the credit principal", type=float)
parser.add_argument("--periods", help="number of payments", type=int)
parser.add_argument("--interest", help="nominal interest rate", type=float)
parser.add_argument("--payment", help="annuity payment", type=int)

args = parser.parse_args()
# print(args)

# i = (args.interest / (12 * 100))

"""
principal = the credit principal
interest = nominal interest rate
periods = number of payments
m = curent period
d = mth differential payment
payment = annuity payment
"""

def diff_payment_cal():
    if args.principal != None and args.periods != None and args.interest != None and args.payment == None:
        sum_payment = 0
        for m in range(1,args.periods + 1):
            d = (args.principal / args.periods) + (args.interest / (12 * 100)) * (args.principal - (args.principal * (m - 1)) / args.periods)
            sum_payment += ceil(d)
            print("Month {}: paid out {}".format(m, ceil(d)))
        overpayment = sum_payment - args.principal
        print("Overpayment = {}".format(ceil(overpayment)))
    else:
        error_incorrect_parameters()

def annuity_payment_cal():
    if args.payment != None and args.interest != None and args.periods != None and args.principal == None:
        principal = args.payment / (((args.interest / (12 * 100)) * pow(1 + (args.interest / (12 * 100)), args.periods)) / (pow(1 + (args.interest / (12 * 100)), args.periods) - 1))
        overpayment = args.payment * args.periods - principal
        print("Your credit principal = {}!".format(floor(principal)))
        print("Overpayment = {}".format(ceil(overpayment)))
    elif args.principal != None and args.periods != None and args.interest != None and args.payment == None:
        payment = args.principal * ((args.interest / (12 * 100)) * pow(1 + (args.interest / (12 * 100)), args.periods)) / (pow(1 + (args.interest / (12 * 100)), args.periods) - 1)
        overpayment = ceil(payment) * args.periods - args.principal
        print("Your annuity payment = {}!".format(ceil(payment)))
        print("Overpayment = {}".format(int(overpayment)))
    elif args.principal != None and args.payment != None and args.interest != None and args.periods == None:
        periods = ceil(log(args.payment / (args.payment - (args.interest / (12 * 100)) * args.principal) , 1 + (args.interest / (12 * 100))))
        # print("period is: {}".format(periods))
        years = periods // 12
        months = periods % 12
        display_period(months=months, years=years)
        overpayment = periods * args.payment - args.principal
        print("Overpayment = {}".format(int(overpayment)))
        
    else:
        error_incorrect_parameters()

def display_period(months, years):
    if months == 1 and years == 0:
        print("You need {} month to repay this credit!".format(months))
    elif months > 1 and years == 0:
        print("You need {} months to repay this credit!".format(months))
    elif months == 0 and years == 1:
        print("You need {} year to repay this credit!".format(years))
    elif months == 0 and years > 1:
        print("You need {} years to repay this credit!".format(years))
    elif months == 1 and years == 1:
        print("You need {} year and {} month to repay this credit!".format(years, months))
    elif months > 1 and years == 1:
        print("You need {} year and {} months to repay this credit!".format(years, months))
    elif months == 1 and years > 1:
        print("You need {} years and {} month to repay this credit!".format(years, months))
    elif months > 1 and years > 1:
        print("You need {} years and {} months to repay this credit!".format(years, months))

def error_incorrect_parameters():
    print("Incorrect parameters")

if args.type == None:
    error_incorrect_parameters()
elif args.type == "diff":
    diff_payment_cal()
elif args.type == "annuity":
    annuity_payment_cal()
else:
    error_incorrect_parameters()

