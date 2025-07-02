# Input list
numbers = [1, 1, 1, 5, 5, 3, 1, 3, 3, 1, 4, 4, 4, 2, 2, 2, 2]

# Create an empty dictionary
freq_dict = {}

# Count frequencies
for num in numbers:
    if num in freq_dict:
        freq_dict[num] += 1
    else:
        freq_dict[num] = 1

# Print the result
for key in sorted(freq_dict):  # optional: sorted output
    print(f"{key} : {freq_dict[key]}", end=" , ")
