class Myclass:
    def prime(self,n):
        if n>1:
            if n%2==0:
                print(n,"is not a prime number")
            else:
                print(n,"is a prime number")
    def pattern(self):
        n = 5
        #diamond pattern
        for i in range(1, n + 1):
            print(" " * (n - i) + "*" * (2 * i - 1))
        for i in range(n - 1, 0, -1):
            print(" " * (n - i) + "*" * (2 * i - 1))
        
            
    def fibonacci(self, n):
        a, b = 0, 1
        print("Fibonacci series:")
        for _ in range(n):
            print(a, end=' ')
            a, b = b, a / b
        print()

ob= Myclass()

while True:
    try:
        n = int(input("Enter a number: "))
        ob.prime(n)
        break
    except ValueError:
        print("\033[91mInvalid input. Please enter a valid integer.\033[0m")
ob.pattern()
ob.fibonacci(10)