<<<<<<< HEAD
def fibonacci_series(n):
    fib_list = []
    a, b = 0, 1
    for _ in range(n):
        fib_list.append(a)
        a, b = b, a + b
    return fib_list

# Input from user
n = int(input("Enter how many Fibonacci numbers to print: "))

# Generate and print
result = fibonacci_series(n)
print("First few Fibonacci numbers are:", ", ".join(map(str, result)))
=======
def fibonacci_series(n):
    fib_list = []
    a, b = 0, 1
    for _ in range(n):
        fib_list.append(a)
        a, b = b, a + b
    return fib_list

# Input from user
n = int(input("Enter how many Fibonacci numbers to print: "))

# Generate and print
result = fibonacci_series(n)
print("First few Fibonacci numbers are:", ", ".join(map(str, result)))
>>>>>>> 6ba82e6219d141262278b73442b64912a104d8bf
