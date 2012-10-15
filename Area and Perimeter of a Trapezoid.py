#Jacob Hayes
#Area of a Trapezoid Calculator

print "*For calculating the Area and Perimeter of a Trapezoid.*"

print "\nEnter only numbers (1, 2, 3, 4 ,5)."

Base_1 = float(raw_input("\nPlease enter the length of the Short Base on the Trapezoid: "))

while not Base_1:
    Base_1 = float(raw_input("Please enter the length of the Short Base on the Trapezoid: "))

Base_2 = float(raw_input("Please enter the length of the Long Base on the Trapezoid: "))

while not Base_2:
    Base_2 = float(raw_input("Please enter the length of the Long Base on the Trapezoid: "))

Left_Side = float(raw_input("Please enter the length of the Left Side on the Trapezoid: "))

while not Left_Side:
    Left_Side = float(raw_input("Please enter the length of the Left Side on the Trapezoid: "))

Right_Side = float(raw_input("Please enter the length of the Right Side on the Trapezoid: "))

while not Base_2:
    Base_2 = float(raw_input("Please enter the length of the Right Side on the Trapezoid: "))


Height = float(raw_input("Please enter the Height of the Trapezoid: "))

while not Height:
    Height = float(raw_input("Please enter the Height of the Trapezoid: "))

Area = ((Base_1 + Base_2) * Height) / 2

print "\nThe Area = ((", Base_1, "+", Base_2, ") x", Height, ") /2"
print "The Area =", Area

raw_input("\nPress enter for the Perimeter.")

Perimeter = Base_1 + Base_2 + Left_Side + Right_Side

print "\nThe Perimeter =", Base_1, "+", Base_2, "+", Left_Side, "+", Right_Side
print "The Perimeter =", Perimeter

raw_input("\nPress enter to exit.")


