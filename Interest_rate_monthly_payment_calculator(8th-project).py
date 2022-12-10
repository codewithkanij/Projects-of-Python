# collect the necessary inputs: principal(initial the loan amount), apr(anual interest rate), years
# calculate the monthly payment
# show to the user

def main():
    print(" This is a monthly payment loan calculator ")
    print("")

      #  program tar calculation  clear na

    principal = float(input("Input the loan amount: "))
    apr = float(input("Input the annual interest rate: "))
    years = int(input("Input amount of years: "))


    monthly_interest_rate = apr / 1200
    amount_of_months = years * 12
    monthly_payment = principal * monthly_interest_rate /(1-(1+monthly_interest_rate) ** (-amount_of_months))

    # print(" The monthly payment for this loan is: " + str(monthly_payment))
    print(" The monthly payment for this loan is: %.2f" + % monthly_payment)  # ekhane ki vul ???



main()

