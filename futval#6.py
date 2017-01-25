#futval.py
# A program to compute the value of an investment
# carried 10 years into the future

def main():
    print("This program calculates the future value")
    print("of a 10-year investment.")

    principal = eval(input("Enter the amount invested each year: "))
    apr = eval(input("Enter the annual interest rate: "))
    years = eval(input("Enter the amount of years: "))
    
    for i in range(years):
        total = principal * (1 + apr)
        total = total + principal

    print("The value in 10 years is:", total)

main()

