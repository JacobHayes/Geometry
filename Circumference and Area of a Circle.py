#Jacob Hayes
#Circumference and Area of a Circle Calculator

print "Circumference and Area of a Circle Calculator"

print "\nWe assume 3.14159 as Pi."

Pi = 3.14159

Radius = float(raw_input("\nPlease enter the radius of the circle: "))

Circumference = 2 * Pi * Radius

print "\nThe Circumference = 2 x Pi x", Radius
print "The Circumference =", Circumference

raw_input("\nPress enter for Area.")

Radius_2 = Radius * Radius
Area = Pi * (Radius_2)

print "\nThe Area = Pi x", Radius, "\b^2"
print "The Area = Pi x", Radius_2
print "The Area =", Area

raw_input("\nPress enter to exit.")

