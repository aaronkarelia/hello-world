#fahrenheit
#This program converts F to C

def main():
    print("This program converts temperatures from F to C.")

    Fahren = eval(input("Enter the temp in Fahrenheit: "))

    celsius = (Fahren - 32) * (5/9)

    print("The Temp in celsius is: ", celsius)

main()
