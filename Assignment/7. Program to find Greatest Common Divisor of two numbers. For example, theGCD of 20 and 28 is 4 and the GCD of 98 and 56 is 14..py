def find_gcd(a, b):
    # Find the smaller of the two numbers
    small = min(a, b)
    
    # Loop from 1 to the smaller number
    for i in range(small, 0, -1):
        if a % i == 0 and b % i == 0:
            return i

# Get input from user
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

# Call the function and print the result
gcd = find_gcd(num1, num2)
print(f"The GCD of {num1} and {num2} is {gcd}")
