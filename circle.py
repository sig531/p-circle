
# Show Area, Circumference, Diameter, Radius, Surface Area, Volume based on any one attribute


# Import sys module to identify version
import sys

# Import math module to perform inbuilt functions
import math
pi = float(math.pi)

if sys.version_info[:1] == (2,):
    print("")
    print("Error:")
    print("    Cause:      Cannot run under Python version 2.")
    print("    Resolution: Install Python version 3 (or higher).")
    print("")
else:
    pass


def get_one_of(prompt, options, default=None):
    options = set(options)
    while True:
        val = input(prompt)
        if val == "" and default is not None:
            return default
        elif val in options:
            return val


def get_radius(choice, value):
    # For each variable, ascertain Radius
    if choice == "a":
        area = value
        radius = math.sqrt(area / pi)
    elif choice == "c":
        circumference = value
        radius = circumference / pi / 2
    elif choice == 'd':
        diameter = value
        radius = diameter / 2
    elif choice == "r":
        radius = value
    elif choice == "s":
        surface_area = value
        radius = math.sqrt(surface_area / 4 / pi)
    elif choice == 'v':
        volume = value
        radius = (volume / (4 / 3) / pi) ** (1 / 3.0)  # ** 1 / 3.0 = Cube Root
    calculate(radius)


def calculate(radius):
    # Derive all variables from Radius
    diameter = radius * 2
    circumference = pi * diameter
    area = pi * (radius ** 2)
    surface_area = 4 * pi * (radius ** 2)
    volume = (4 / 3) * pi * (radius ** 3)
    output_results(radius, diameter, area, circumference, volume, surface_area)


def output_results(radius, diameter, area, circumference, volume, surface_area):
    # Output results
    print()
    print("GENERAL:")
    print(" . radius:        ", radius)
    print("CIRCLE:")
    print(" . diameter:      ", diameter)
    print(" . area:          ", area)
    print(" . circumference: ", circumference)
    print("SPHERE:")
    print(" . volume:        ", volume)
    print(" . surface area:  ", surface_area)
    print()


def display_error(value):
    # Error handling variables
    error_title = "Error:"
    error_cause = "    Cause:      Cannot ascertain results for value = '%s'." % value
    error_resolution = "    Resolution: Value must be a positive number."

    print()
    print(error_title)
    print(error_cause)
    print(error_resolution)
    print()

def get_choice():
    print()
    raw_input = get_one_of("Enter variable - (a)rea, (c)ircumference, (d)iameter, (r)adius, (s)urface area, (v)olume "
                           "[r]: ", "aAcCdDrRsSvV", "r")
    choice = raw_input.lower()

    if choice == "a":
        variable = "area"
    elif choice == "c":
        variable = "circumference"
    elif choice == 'd':
        variable = "diameter"
    elif choice == "r":
        variable = "radius"
    elif choice == "s":
        variable = "surface area"
    elif choice == "v":
        variable = "volume"
    else:
        variable = "<unknown>"
    get_value(choice, variable)


def get_value(choice, variable):
    value = input("Enter %s: " % variable)

    try:
        value = float(value)
    except ValueError:  # Report error if value entered is not an integer (however,
        # value entered can be positive or negative)
        display_error(value)
    else:
        value = float(value)
        if value < 0:  # Report error if value entered is not a positive number
            display_error(value)
        else:  # Only proceed if a value entered is a positive number
            get_radius(choice, value)


get_choice()
