#Jacob Hayes
#Area of a Trapezoid Calculator

print "*For calculating the Area and Perimeter of a Triangle.*"


Base = float(raw_input("\nEnter the Length of the Base: "))

while not Base:
    Base = float(raw_input("Enter the Length of the Base: "))

Left_Length = float(raw_input("\nEnter the Length of the Left Side: "))

while not Left_Length:
    Left_Length = float(raw_input("Enter the Length of the Left Side: "))

Right_Length = float(raw_input("\nEnter the Length of the Right Side: "))

while not Right_Length:
    Right_Length = float(raw_input("Enter the Length of the Right Side: "))

Height = float(raw_input("\nEnter the Length of the Height: "))

while not Height:
    Height = float(raw_input("Enter the Length of the Height: "))

Area = .5 * (Base * Height)

print "\nThe Area is 1/2(", Base, "*", Height, ")"
print "The Area is", Area

raw_input("\nPress enter for the Perimeter")

Perimeter = Base + Left_Length + Right_Length

print "\nThe Perimeter is", Base, "+", Left_Length, "+", Right_Length
print "The Perimeter is", Perimeter

raw_input("\nPress enter to exit")
