"""volume conversion python program
it takes number of arguments
and use dictionary as conversion factor for scalability
"""
# the conversion_factors represent how many LITERS are in 1 of these units
conversion_factor = {
    # Metric
    "ml": 0.001,
    "cl": 0.01,
    "l": 1.0,
    "m3": 1000.0,

    # US/Imperial
    "fl_oz": 0.0295735,
    "cup": 0.236588,
    "pints": 0.473176,
    "quarts": 0.946353,
    "gallons": 3.78541,

    # Cooking
    "tsp": 0.00492892,
    "tbsp": 0.0147868

    }
def volume_converter(value, from_unit, to_unit):
    # check if the unit is Exist in our unit
    if from_unit  not in conversion_factor or to_unit not in conversion_factor:
        return None
    else:
        # convert to liters
        unit_in_liters = value * conversion_factor[from_unit]
        #  convert to the asked unit
        result =  unit_in_liters * (1/conversion_factor[to_unit])
        return result
print ("=======WELCOME TO THE VOLUTION CONVERTOR======")
while True:
    try:
        value = float(input("Enter your value: "))
        from_unit = input("Fom unit: ").lower().strip()
        to_unit = input("To unit: ").lower().strip()
        volume = volume_converter(value, from_unit, to_unit)
        if volume is None:
            print("Error: One or both of the units you entered is not supported.")
        else:
            print(f"Result : {round(volume,2)}{to_unit}")
            print()
            choice = input("Would you like to use again? Enter y if YES or N if NO (y/n): ").lower().strip()
            if choice == "y":
                continue
            else:
                print("Goodbye")
                break
    except ValueError:
            print("Error: Please enter a valid number for the value.")
