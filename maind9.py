# 1. **Age Calculator** — input birth year, output age
# 2. **Greeting Program** — input name → print greeting
# 3. **Simple Calculator** — addition, subtraction, multiplication, division
# 4. **String Reverse & Counter** — reverse user input & count letters
# 5. **User Profile Summary** — combine variables, input, strings
# ----------1
import datetime


# ----------2  **Greeting Program** — input name → print greeting
def greeting_program(name):
    return f"Hello, {name}!"


try:
    user_name = input("Enter your name. only string: ").upper()

    greeting_program(user_name)
    print(greeting_program(user_name))
except ValueError:
    print("Invalid input. Please enter a correct name.")

import datetime


def calculate_exact_age(birth_year, birth_month, birth_day):
    """Calculates the precise age in years based on a full date of birth."""
    today = datetime.date.today()
    birth_date = datetime.date(birth_year, birth_month, birth_day)
    age = today.year - birth_date.year

    # Logic to adjust age if the birthday is later in the year
    if today < datetime.date(today.year, birth_date.month, birth_date.day):
        age -= 1

    return age


# --- Main Program Execution with Error Handling ---
try:
    print("Please enter your date of birth.")
    # 1. Get all three inputs and convert to integers
    birth_year = int(input("Enter birth year (YYYY): "))
    birth_month = int(input("Enter birth month (1-12): "))
    birth_day = int(input("Enter birth day (1-31): "))

    # 2. Call the function
    current_age = calculate_exact_age(birth_year, birth_month, birth_day)

    # 3. Display the result
    print(f"\nYour precise age is: {current_age} years old! 🥳")

# Handle potential errors from bad input (ValueError) or invalid dates (e.g., February 30th)
except ValueError as e:
    print(
        f"\nOops! An error occurred. Please ensure you entered valid whole numbers for the dates, and that the date itself is valid (e.g., month 1-12, day 1-31). Details: {e}")


# ---------------- 3) **Simple Calculator** — addition, subtraction, multiplication, division

def simple_calculator(num1, operator, num2):
    sum = num1 + num2
    sub = num1 - num2
    mul = num1 * num2
    div = num1 / num2
    if operator == '+':
        return sum
    elif operator == '-':
        return sub

    elif operator == '*':
        return mul
    elif operator == '/':
        return div


try:
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    operator = input("Enter operator: +, -, *, / : ")
    result = simple_calculator(num1, operator, num2)
    print(f"the result is {result}")
except ZeroDivisionError:
    print("division error")
except ValueError:
    print("value error")


# --------------4. **String Reverse & Counter** — reverse user input & count letters

def reverse_and_count(input_string):
    """
    Reverses the input string and counts the total number of letters (A-Z, a-z).
    """
    # 1. String Reversal
    # Uses slicing [::-1] which is a Python idiomatic way to reverse a sequence
    reversed_string = input_string[::-1]

    # 2. Letter Counter
    letter_count = 0
    for char in input_string:
        # The .isalpha() method checks if all characters in the string are
        # alphabetical (a-z and A-Z) and there is at least one character.
        if char.isalpha():
            letter_count += 1

    # Return the results
    return reversed_string, letter_count


# --- Main Program Execution ---

# Get input from the user
user_input = input("Enter a string (e.g., 'Hello World 123!'): ")

# Call the function
reversed_text, count = reverse_and_count(user_input)

# Display the results
print("\n--- Results ---")
print(f"Original String: {user_input}")
print(f"Reversed String: {reversed_text}")
print(f"Total Letters (A-Z, a-z) Count: {count}")

