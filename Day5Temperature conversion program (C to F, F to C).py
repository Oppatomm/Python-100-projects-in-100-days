print("=== Temperature conversion program (C to F, F to C) ===")
while True :
    number =  input("1. Celsius to Fahrenheit\n"
                    "2. Fahrenheit to Celsius\n"
                    "Select (1 - 2) : ")

    if  not number.isdigit() :
        print("Please enter numbers only.")
        continue
    else :
        num = int(number)

        if num == 1  :
            c = int(input("Please enter temperature (Celsius) : "))
            celsius = (c * 9/5) + 32
            print(f"{int(c)}\u00B0C = {int(celsius)}\u00B0F")
        elif num == 2 :
            f = float(input("Please enter temperature (Fahrenheit) : "))
            fahrenheit = (f - 32) * 5/9
            print(f"{f}\u00B0F = {int(fahrenheit)}\u00B0C")
        else :
            print("Please enter 1 or 2 numbers only.") 
            continue       
        

    choose = input("Want to convert again? (y / n) : ") 

    if choose == 'y' :
        continue
    elif choose == 'n' :
        print("Thank you for using the service.")
        break