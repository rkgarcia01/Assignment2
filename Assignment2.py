# Name: Reyki Garcia
# NetID: rkg134
# Github Username: RixGarcia
import re

# This function tells you what category you BMI is in
def BMI_Category(BMI):
    BMI_Ans = ""
    if BMI < 18.5:
        BMI_Ans = "Underweight"
    elif 18.5 <= BMI and BMI <= 24.9:
        BMI_Ans = "Normal Weight"
    elif 25.0 <= BMI and BMI <= 29.9:
        BMI_Ans = "Overweight"
    elif 30 <= BMI:
        BMI_Ans = "Obese"
    else:
        return
    return BMI_Ans


# This function converts the pounds to kilograms and returns the value
def BMI_Weight_Converter(BMI_Pounds):
    Kilograms = BMI_Pounds * 0.45
    return Kilograms


# This function converts the feet into inches
# The function then converts the inches to meters.
def BMI_Height_Converter(BMI_Height):
    Height = BMI_Height.split("'")
    Feet = int(Height[0])
    Inches = Height[1]
    regex = "\d"
    Real_Inches = re.findall(regex, Inches)
    # Real_Inches2 = int(Real_Inches[0])
    Total_Inches = (Feet * 12) + int(Real_Inches[0])
    Meters = Total_Inches * 0.025
    Meters_Rounded = round(Meters, 3)
    Meters_Squared = Meters_Rounded**2
    return Meters_Squared


# This is the main function that calls all the other function
# It starts with the user's inputs
def main():
    print("Welcome to obtaining your BMI application")
    BMI_Pounds = int(input("Enter in your weight (in pounds): "))
    BMI_Height = input("Enter in your height in feet and inches (e.g., '5'3' seperate with '''): ")
    BMI_Weight_Converted = BMI_Weight_Converter(BMI_Pounds)
    BMI_Height_Converted = BMI_Height_Converter(BMI_Height)
    BMI = round(BMI_Weight_Converted / BMI_Height_Converted, 1)
    BMI_Range = BMI_Category(BMI)
    print("This is your Body Mass Index (BMI): ", BMI_Range)


# This tells it to go to the main() function first
if __name__ == "__main__":
    main()
