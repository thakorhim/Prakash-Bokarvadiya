def swap_first_two_chars(str1, str2):
    # If either string has less than 2 characters, return as is
    if len(str1) < 2 or len(str2) < 2:
        return "Both strings must have at least two characters."

    # Swap first two characters
    new_str1 = str2[:2] + str1[2:]
    new_str2 = str1[:2] + str2[2:]

    # Return the combined result
    return new_str1 + " " + new_str2

# Get input from the user
string1 = input("Enter first string: ")
string2 = input("Enter second string: ")

# Call the function and print result
result = swap_first_two_chars(string1, string2)
print("Result:", result)
