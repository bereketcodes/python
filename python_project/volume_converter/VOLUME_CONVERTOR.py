import tkinter as tk
from tkinter import messagebox

# Step 1: Create conversion table (to liter)
units = {
    "Liter (L)": 1,
    "Milliliter (mL)": 0.001,
    "Centiliter (cL)": 0.01,
    "Deciliter (dL)": 0.1,
    "Hectoliter (hL)": 100,
    "Kiloliter (kL)": 1000,
    "Cubic centimeter (cm³)": 0.001,
    "Cubic decimeter (dm³)": 1,
    "Cubic meter (m³)": 1000,
    "US gallon": 3.78541,
    "US quart": 0.946353,
    "US pint": 0.473176,
    "US cup": 0.236588,
    "Fluid ounce": 0.0295735
}

# Step 2: Define conversion function
def convert_volume():

    # Get value from entry box
    value_text = entry_value.get()

    # Check if input is empty
    if value_text == "":
        messagebox.showerror("Error", "Please enter a value")
        return

    # Try converting input to number
    try:
        value = float(value_text)
    except ValueError:
        messagebox.showerror("Error", "Value must be a number")
        return

    # Check for negative value
    if value < 0:
        messagebox.showerror("Error", "Volume cannot be negative")
        return

    # Get selected units
    from_unit = from_unit_var.get()
    to_unit = to_unit_var.get()

    # Convert to liters
    value_in_liter = value * units[from_unit]

    # Convert to target unit
    result = value_in_liter / units[to_unit]

    # Display result
    label_result.config(text="Result: " + str(result))

# Step 3: Create main window
window = tk.Tk()
window.title("Volume Converter")

# Step 4: Create labels and input box
tk.Label(window, text="Enter volume value").grid(row=0, column=0, padx=5, pady=5)
entry_value = tk.Entry(window)
entry_value.grid(row=0, column=1)

# Step 5: From unit selection
tk.Label(window, text="From unit").grid(row=1, column=0, padx=5, pady=5)
from_unit_var = tk.StringVar()
from_unit_var.set("Liter (L)")
tk.OptionMenu(window, from_unit_var, *units.keys()).grid(row=1, column=1)

# Step 6: To unit selection
tk.Label(window, text="To unit").grid(row=2, column=0, padx=5, pady=5)
to_unit_var = tk.StringVar()
to_unit_var.set("Milliliter (mL)")
tk.OptionMenu(window, to_unit_var, *units.keys()).grid(row=2, column=1)

# Step 7: Convert button
tk.Button(window, text="Convert", command=convert_volume).grid(row=3, column=1, pady=10)

# Step 8: Result label
label_result = tk.Label(window, text="Result:")
label_result.grid(row=4, column=0)

# Step 9: Run the program
window.mainloop()
