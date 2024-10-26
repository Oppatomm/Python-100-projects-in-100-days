print("=== Basic calculator ===")
choose =  int(input("Please choose your choice.\n"
                    "1 means addition (+)\n"
                    "2 means subtraction (-)\n"
                    "3 means multiplication (*)\n"
                    "4 means division (/)\n"
                    "Example Input : 1\n")
            )
number1 = int(input("Number 1 : "))
number2 = int(input("Number 2 : "))

match choose :
    case 1 :
        print(f"{number1} + {number2} = {number1 + number2}")
    case 2 :
        print(f"{number1} - {number2} = {number1 - number2}")
    case 3 :
        print(f"{number1} * {number2} = {number1 * number2}")
    case 4 :
        if number2 != 0 :
            print(f"{number1} / {number2} = {number1 / number2}")
        else :
            print("Cannot divide by zero.")
    case _ :
        print("You entered incorrectly Please try again.")