# even_odd_checker_functions.py

def get_integer_input() -> int:
    """
    Prompts the user to enter an integer and returns the integer after validation.
    Repeats the prompt until a valid integer is entered.

    Returns:
        int: The valid integer entered by the user.
    """
    while True:
        try:
            number = int(input("Enter an integer: "))  # Attempt to convert input to integer
            return number  # Return the valid integer
        except ValueError:  # Catch the exception if input is not a valid integer
            print("Invalid input. Please enter a valid integer.")

def check_even_odd(number: int) -> str:
    """
    Checks whether a given number is even or odd.

    Args:
        number (int): The number to be checked.

    Returns:
        str: A formatted string indicating if the number is "Even" or "Odd".
    """
    if number % 2 == 0:
        return f"{number} is an Even number."
    else:
        return f"{number} is an Odd number."

def main():
    # Get an integer input from the user
    number = get_integer_input()

    # Check if the number is even or odd and display the result
    result = check_even_odd(number)
    print(result)

if __name__ == "__main__":
    main()
