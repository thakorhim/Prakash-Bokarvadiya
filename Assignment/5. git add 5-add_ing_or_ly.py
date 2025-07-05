<<<<<<< HEAD
def add_ing_or_ly(word):
    if len(word) < 3:
        return word
    elif word.endswith("ing"):
        return word + "ly"
    else:
        return word + "ing"

# Input from user
text = input("Enter a word: ")
result = add_ing_or_ly(text)
print("Result:", result)
=======
def add_ing_or_ly(word):
    if len(word) < 3:
        return word
    elif word.endswith("ing"):
        return word + "ly"
    else:
        return word + "ing"

# Input from user
text = input("Enter a word: ")
result = add_ing_or_ly(text)
print("Result:", result)
>>>>>>> 6ba82e6219d141262278b73442b64912a104d8bf
