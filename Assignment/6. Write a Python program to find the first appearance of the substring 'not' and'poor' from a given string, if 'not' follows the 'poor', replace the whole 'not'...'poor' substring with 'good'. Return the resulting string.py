def replace_not_poor_with_good(sentence):
    not_index = sentence.find('not')
    poor_index = sentence.find('poor')

    if not_index != -1 and poor_index != -1 and not_index < poor_index:
        return sentence[:not_index] + 'good' + sentence[poor_index + 4:]
    else:
        return sentence

# Input from user
text = input("Enter a sentence: ")
result = replace_not_poor_with_good(text)
print("Result:", result)
