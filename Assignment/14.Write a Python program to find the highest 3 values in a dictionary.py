# Sample dictionary
my_dict = {'a': 50, 'b': 80, 'c': 45, 'd': 100, 'e': 65}

# Sort dictionary items by value in descending order
sorted_items = sorted(my_dict.items(), key=lambda item: item[1], reverse=True)

# Get top 3 items
top_3 = sorted_items[:3]

# Print the top 3 values
print("Top 3 highest values:")
for key, value in top_3:
    print(f"{key}: {value}")
