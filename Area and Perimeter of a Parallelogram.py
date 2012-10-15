#Jacob Hayes
#Area of a Parallelogram Calculator

print "\n\nArea and Perimeter of a Parallelogram"

Base = float(raw_input("\nPlease enter the base of the parallelogram: "))

while not Base:
    Base = float(raw_input("Please enter the base of the parallelogram: "))

Height = float(raw_input("Please enter the height of the parallelogram: "))

while not Height:
    Height = float(raw_input("Please enter the height of the parallelogram: "))

Area = Base * Height

print "\nThe Area =", Base, "x", Height
print "The Area =", Area

raw_input("\nPress enter for Perimeter.")

Perimeter = Base + Height
Perimeter = 2 * Perimeter

print "\nThe Perimeter = 2(", Base, "+", Height, ")"
print "The Perimeter =", Perimeter

raw_input("\nPress enter to exit")
