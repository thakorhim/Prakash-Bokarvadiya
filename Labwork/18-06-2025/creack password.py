# Simulated hidden password (in real, this will be hidden from us)

hidden_password =input("Enter Password :")

# Function to check each letter
def check_letter(char, pos):
    if pos < len(hidden_password):
        return hidden_password[pos] == char
    else:
        return False

# Function to reconstruct password
def find_password():
    found_password = ""
    
    # Let's assume max password length is 20
    for pos in range(20):
        found = False
        for ascii_code in range(32, 127):  # All printable characters
            char = chr(ascii_code)
            if check_letter(char, pos):
                found_password += char
                print(f"Found at pos {pos}: {char}")
                found = True
                break
        if not found:
            break  # No more characters found
    return found_password

# Final Output
recovered_password = find_password()
print("Recovered Password:", recovered_password)
