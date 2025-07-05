<<<<<<< HEAD
def find_second_smallest(numbers):
    # Remove duplicates
    unique_numbers = list(set(numbers))

    # Check if there are at least two unique numbers
    if len(unique_numbers) < 2:
        return "List must contain at least two unique numbers."

    # Sort the list
    unique_numbers.sort()

    # Return the second smallest
    return unique_numbers[1]

# Example list
num_list = [10, 20, 4, 4, 10, 5, 1]

# Call the function
result = find_second_smallest(num_list)
print("Second smallest number is:", result)
=======
def find_second_smallest(numbers):
    # Remove duplicates
    unique_numbers = list(set(numbers))

    # Check if there are at least two unique numbers
    if len(unique_numbers) < 2:
        return "List must contain at least two unique numbers."

    # Sort the list
    unique_numbers.sort()

    # Return the second smallest
    return unique_numbers[1]

# Example list
num_list = [10, 20, 4, 4, 10, 5, 1]

# Call the function
result = find_second_smallest(num_list)
print("Second smallest number is:", result)
>>>>>>> 6ba82e6219d141262278b73442b64912a104d8bf
