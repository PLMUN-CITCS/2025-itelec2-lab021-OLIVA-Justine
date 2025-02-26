"""
factorial_calculator_functions.py

This program calculates the factorial of a given non-negative integer.
It consists of two functions:
1. get_non_negative_integer() - Handles user input and validation.
2. calculate_factorial(n) - Computes the factorial of the given number.
"""

def get_non_negative_integer() -> int:
    """
    Prompt the user to enter a valid non-negative integer.

    Returns:
        int: The validated non-negative integer input by the user.
    """
    while True:
        try:
            number = int(input("Enter a non-negative integer: "))  # User input
            if number < 0:
                print("Error: Please enter a non-negative integer.")  # Check negative input
            else:
                return number  # Return the validated integer
        except ValueError:
            print("Error: Invalid input. Please enter a valid integer.")  # Check non-integer input

def calculate_factorial(n: int) -> int:
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
    return factorial  # Return the calculated factorial

if __name__ == "__main__":
    # Main Program Flow
    number = get_non_negative_integer()
    result = calculate_factorial(number)  # Compute factorial
    print(f"The factorial of {number} is: {result}")  # Display the result
