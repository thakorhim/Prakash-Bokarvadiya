class A:
    def fact(self):
        n = 5
        fact = 1
        for i in range(1, n + 1):
            fact = fact * i
        print(fact)
class B(A):
    def prime(self):
        n = 7
        is_prime = True
        for i in range(2, n):
            if n % i == 0:
                is_prime = False
                break
        if is_prime:
            print(n, "is a prime number")
        else:
            print(n, "is not a prime number")
class C(B):
    def fabonacci(self):
        n=10
        a,b= 0, 1
        print("Fibonacci series:")
        for i in range(n):
            print(a, end=" ")
            a, b = b, a + b
        print()

obj = C()
obj.fact()
obj.prime()
