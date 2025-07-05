<<<<<<< HEAD
import math

# Function to calculate sum of odd series
def odd_series_sum(n):
    sum_odd = 0
    for i in range(1, n + 1, 2):  # odd numbers
        term = (i ** 2) / math.factorial(i)
        sum_odd += term
    return sum_odd

# Function to calculate sum of even series
def even_series_sum(n):
    sum_even = 0
    for i in range(2, n + 1, 2):  # even numbers
        term = (i ** 2) / math.factorial(i)
        sum_even += term
    return sum_even

# Main program
n = int(input("Enter the value of n (max term number): "))

# Calculate and display both series
odd_sum = odd_series_sum(n)
even_sum = even_series_sum(n)

print(f"\nSum of Odd Series up to {n}: {odd_sum:.4f}")
print(f"Sum of Even Series up to {n}: {even_sum:.4f}")
=======
import math

# Function to calculate sum of odd series
def odd_series_sum(n):
    sum_odd = 0
    for i in range(1, n + 1, 2):  # odd numbers
        term = (i ** 2) / math.factorial(i)
        sum_odd += term
    return sum_odd

# Function to calculate sum of even series
def even_series_sum(n):
    sum_even = 0
    for i in range(2, n + 1, 2):  # even numbers
        term = (i ** 2) / math.factorial(i)
        sum_even += term
    return sum_even

# Main program
n = int(input("Enter the value of n (max term number): "))

# Calculate and display both series
odd_sum = odd_series_sum(n)
even_sum = even_series_sum(n)

print(f"\nSum of Odd Series up to {n}: {odd_sum:.4f}")
print(f"Sum of Even Series up to {n}: {even_sum:.4f}")
>>>>>>> 6ba82e6219d141262278b73442b64912a104d8bf
