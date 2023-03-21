# from Assignment2 import BMI_Category
import Assignment2

# These 4 funcrtions test the BMI range and tells if it is Underweight, Normal Weight, Overweight, or Obese
def test_BMI_Category_NormalWeight():
    assert Assignment2.BMI_Category(18.5) == "Normal Weight"


def test_BMI_Category_UnderWeight():
    assert Assignment2.BMI_Category(18.4) == "Underweight"


def test_BMI_Category_Overweight():
    assert Assignment2.BMI_Category(25.1) == "Overweight"


def test_BMI_Category_Obese():
    assert Assignment2.BMI_Category(30.1) == "Obese"


# This function tests if the pounds convert to kilograms correctly
def test_BMI_Weight_Converter():
    assert Assignment2.BMI_Weight_Converter(125) == 56.25


# This functions tests if the heights converts the feet to meters correcrtly
def test_BMI_Height_Converter():
    assert Assignment2.BMI_Height_Converter("5'3") == 2.480625

