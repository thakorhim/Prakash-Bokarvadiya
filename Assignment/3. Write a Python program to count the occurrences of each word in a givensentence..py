# Get input from the user
sentence = input("Enter a sentence: ")

# Convert the sentence to lowercase to make the count case-insensitive
sentence = sentence.lower()

# Split the sentence into words
words = sentence.split()

# Create an empty dictionary to store word counts
word_count = {}

# Loop through each word in the list
for word in words:
    # If the word is already in dictionary, increment count
    if word in word_count:
        word_count[word] += 1
    else:
        # If not in dictionary, add it with count 1
        word_count[word] = 1

# Print the word counts
print("\nWord Occurrences:")
for word, count in word_count.items():
    print(f"{word}: {count}")
