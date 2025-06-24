 # Python program to count occurrences of a substring in a string

# Take input from the user
main_string = input("Enter the main string: ")
substring = input("Enter the substring to count: ")
count = main_string.count(substring)                                      # Count occurrences using count() method
print(f"The substring '{substring}' appears {count} times in the string.")   # Display the result
