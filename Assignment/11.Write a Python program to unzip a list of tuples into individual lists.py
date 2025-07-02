# Example list of tuples
zipped_list = [(1, 'a'), (2, 'b'), (3, 'c')]

# Use zip(*) to unzip
list1, list2 = zip(*zipped_list)

# Convert result to lists
list1 = list(list1)
list2 = list(list2)

# Print the results
print("First list:", list1)
print("Second list:", list2)
