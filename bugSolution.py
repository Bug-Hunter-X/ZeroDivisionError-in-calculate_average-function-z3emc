def calculate_average(numbers):
    if not numbers:  # Check for empty list
        return 0  # Return 0 for an empty list
    total = sum(numbers)
    average = total / len(numbers)
    return average

my_numbers = []
result = calculate_average(my_numbers)
print(f"The average is: {result}")  # Output: The average is: 0

my_numbers = [10, 20, 30]
result = calculate_average(my_numbers)
print(f"The average is: {result}")  # Output: The average is: 20.0