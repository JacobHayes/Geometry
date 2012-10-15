#Jacob Hayes
#Volume and Surface Area of a Rectangular Prism

print "Volume and Surface Area of a Rectangular Prism"

Length = float(raw_input("\nPlease enter the Length of the Prism: "))
Width = float(raw_input("Please enter the Width of the Prism: "))
Height = float(raw_input("Please enter the Height of the Prism: "))

Volume = Length * Width * Height

print "\nThe Volume =", Length, "x", Width, "x", Height
print "The Volume =", Volume

raw_input("\nPress enter for Surface Area")

SA = 2 * ((Length * Width) + (Height * Width) + (Height * Length))

print "\nThe Surface Area = 2 x (", Length, "x", Width, "+", Height, "x", Width, "+", Height, "x", Length
print "The Surface Area =", SA

raw_input("\nPress enter to exit.")
