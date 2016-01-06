'''
Show Area, Circumference, Diameter, Radius, Surface Area, Volume based on any one attribute
'''

#Import sys module to identify version
import sys

if sys.version_info[:1] == (2,):
    print("")
    print("Error:")
    print("    Cause:      Cannot run under Python version 2.")
    print("    Resolution: Install Python version 3 (or higher).")
    print("")
else:
    #Import math module to perform inbuilt functions
    import math

def get_one_of(prompt, options, default=None):
    options = set(options)
    while True:
        val = input(prompt)
        if val == "" and default is not None:
            return default
        elif val in options:
            return val

print()
RawInput = get_one_of("Enter variable - (a)rea, (c)ircumference, (d)iameter, (r)adius, (s)urface area, (v)olume [r]: ", "aAcCdDrRsSvV", "r")
Choice = RawInput.lower()

if Choice == "a":
    Variable = "area"
elif Choice == "c":
    Variable = "circumference"
elif Choice == 'd':
    Variable = "diameter"
elif Choice == "r":
    Variable = "radius"
elif Choice == "s":
    Variable = "surface area"
elif Choice == "v":
    Variable = "volume"
else:
    Variable == "<undefined>"

Value = input("Enter %s: " % Variable)

#Error handling variables
ErrorTitle = "Error:"
ErrorCause = "    Cause:      Cannot ascertain results for value = '%s'." % Value #"    Cause:      Cannot ascertain results for value = '" + str(Value) + "'."
ErrorResolution = "    Resolution: Value must be a positive number."

try:
    Value = float(Value)
except ValueError: #Report error if value entered is not an integer (however, value entered can be positive or negative)
    print()
    print(ErrorTitle)
    print(ErrorCause)
    print(ErrorResolution)
    print()
else:  
    Value = float(Value)
    if Value < 0: #Report error if value entered is not a positive number
        print()
        print(ErrorTitle)
        print(ErrorCause)
        print(ErrorResolution)
        print()
    else: #Only proceed if a value entered is a positive number
    
        Pi = float(math.pi)
    
        #For each variable, ascertain Radius
        if Choice == "a":
            Area = Value
            Radius = math.sqrt(Area / Pi)
        elif Choice == "c":
            Circumference = Value
            Radius = Circumference / Pi / 2
        elif Choice == 'd':
            Diameter = Value
            Radius = Diameter / 2
        elif Choice == "r":
            Radius = Value
        elif Choice == "s":
            SurfaceArea = Value
            Radius = math.sqrt(SurfaceArea / 4 / Pi)
        elif Choice == 'v':
            Volume = Value
            Radius = (Volume / (4 / 3) / Pi) ** (1 / 3.0) # ** 1 / 3.0 = Cube Root

        #Derive all variables from Radius
        Diameter = Radius * 2
        Circumference = Pi * Diameter
        Area = Pi * (Radius ** 2)
        SurfaceArea = 4 * Pi * (Radius ** 2)
        Volume = (4 / 3) * Pi * (Radius ** 3)

        #Output results
        print()
        print("GENERAL:")
        print(" . radius:        ", Radius)
        print("CIRCLE:")
        print(" . diameter:      ", Diameter)
        print(" . area:          ", Area)
        print(" . circumference: ", Circumference)
        print("SPHERE:")
        print(" . volume:        ", Volume)
        print(" . surface area:  ", SurfaceArea)
        print()
