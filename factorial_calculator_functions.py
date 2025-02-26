def get_non_negative_integer() -> int:
    """
    Prompt the user to enter a valid integer.

    Returns:
        int: The validated integer input by the user.
    """
    while True:  # Fixed syntax error (true -> True)
        try:
            number = int(input("Enter a non-negative integer: "))
            return number
        except ValueError:
            print("Error: Invalid input. Please enter a valid integer.")

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
    return factorial

# Main Program Flow
if __name__ == "__main__":
    number = get_non_negative_integer()
    result = calculate_factorial(number)
    print(f"The factorial of {number} is: {result}")
