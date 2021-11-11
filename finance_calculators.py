import math

# This is a program that allows the user to access two different types of financial calculators
# First move is to ask the user to choose between an investment calculator or a bond repayment calculator

# Setting variables for the 4 inputs we are looking for in the program

x = 'investment'
y = 'bond'
a = 'simple'
b = 'compound'

user_option = input('''Choose either 'investment' or 'bond' from the menu below to proceed:\n
investment - to calculate the amount of interest you'll earn on interest\n
bond - to calculate the amount you'll have to pay on a home loan\n
: ''').lower()  # this will ensure the user's input is accepted regardless of how the word is typed

if user_option == x:
    user_amount = float(input("Enter the amount of money that you will be depositing R: "))
    user_interest = float(input("Enter the interest rate that you want (%): "))
    user_interest = user_interest / 100  # we are doing this to get the interest number as a percentage
    user_years = int(input("Enter the number of years you plan on investing for: "))

    interest = input("Type in the interest that you would like - 'Simple or 'Compound': ").lower()
    if interest == a:
        simple_int = user_amount * (1 + user_interest * user_years)
        simple_int = round(simple_int, 2)  # rounding number to 2 decimal places
        print(f"Simple interest is R{simple_int}")
    elif interest == b:
        compound_int = user_amount * math.pow((1 + user_interest), user_years)
        compound_int = round(compound_int, 2)
        print(f"Compound interest is R{compound_int}")

elif user_option == y:
    house_value = float(input("Enter the present value of the house: "))
    user_interest = float(input("Enter the interest rate that you want (%): "))
    user_interest /= 100  # calculating the interest rate percentage
    monthly_interest = user_interest / 12  # calculating monthly interest
    user_months = int(input("enter the number of months you want to take: "))
    bond_amnt = (monthly_interest * house_value) / (1 - math.pow((1 + monthly_interest), -user_months))
    bond_amnt = round(bond_amnt, 2)
    print(f"Amount to be paid per month is R{bond_amnt}")

else:
    print(f"ERROR MESSAGE: Kindly rerun the program and only select either '{x}' or '{y}.'")
