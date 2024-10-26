print("=== BMI calculation program ===")
height = int(input("Height : "))
weight = int(input("Weight : "))
cm_convert_m = height / 100
height_multiply_height = cm_convert_m * cm_convert_m
bmi = weight / height_multiply_height
bmi = round(bmi,2)
if bmi > 30 : 
    print(str(bmi) + " : Obesity")
elif bmi <= 29.9 and bmi >= 25 :
    print(str(bmi) + " : Overweight")
elif bmi <= 24.9 and bmi >= 18.5 :
    print(str(bmi) + " : Normal weight")
else :
    print(str(bmi) + " : Underweight")