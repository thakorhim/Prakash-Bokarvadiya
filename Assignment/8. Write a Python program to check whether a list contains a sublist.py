<<<<<<< HEAD
def contains_sublist(main_list, sub_list):
    sub_length = len(sub_list)
    
    # Loop through the main list
    for i in range(len(main_list) - sub_length + 1):
        # Check if the current slice matches the sublist
        if main_list[i:i + sub_length] == sub_list:
            return True
    return False

# Example lists
main_list = [1, 2, 3, 4, 5, 6]
sub_list = [3, 4, ]

# Check if sublist is present
if contains_sublist(main_list, sub_list):
    print("Sublist is present in the main list.")
else:
    print("Sublist is not present in the main list.")
=======
def contains_sublist(main_list, sub_list):
    sub_length = len(sub_list)
    
    # Loop through the main list
    for i in range(len(main_list) - sub_length + 1):
        # Check if the current slice matches the sublist
        if main_list[i:i + sub_length] == sub_list:
            return True
    return False

# Example lists
main_list = [1, 2, 3, 4, 5, 6]
sub_list = [3, 4, ]

# Check if sublist is present
if contains_sublist(main_list, sub_list):
    print("Sublist is present in the main list.")
else:
    print("Sublist is not present in the main list.")
>>>>>>> 6ba82e6219d141262278b73442b64912a104d8bf
