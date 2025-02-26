"""
factorial_calculator_factions.py

This part tell if the user input is even or odd
It consists two functions:
1. get_non_ integer() - Handle user input and validation.
2. calculate_factorial(n) - check if the number is even or odd.
"""
def get_non_negative_integer() -> int:
    """
    Prompt the user to enter a valid integer.

    Returns:
        int: The validated integer input by the user.
    """
    while True:  # Fixed syntax error (true -> True)
        try:
            number = int(input("Enter a non-negative integer: ")) # User input
            return number # Return the validated integer
        except ValueError:
            print("Error: Invalid input. Please enter a valid integer.") # check non-integer input

def calculate_factorial(n):
    """
    Calculates the factorial of a given non-negative integer.
    Args:
        n (int): Non-negative integer.
    Returns:
        int: Factorial of n.
    """
    if n == 0:
        return 1 
    factorial = 1
    for i in range(1, n + 1):
        factorial *= i
    return factorial # return the calculated factorial


if __name__ == "__main__":
	# Main Program Flow
    number = get_non_negative_integer()
    result = calculate_factorial(number) # Check the result status
    print(f"The factorial of {number} is: {result}") # Display the result
