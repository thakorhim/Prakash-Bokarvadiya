class a:
    def prime(self):
        n=5
        for i in range(2,n):
            if n%i==0:
                print("Not prime")
                break
        else:
            print("Prime")

class b(a):
    n=5
    def fact(self):
        fact=1
        for i in range(1,self.n+1):
            fact*=i
        print("Factorial:",fact)

class c:
    def feb(self):
        a=0
        b=1
        print("Fibonacci Series:")
        for i in range(5):
            print(a)
            c=a+b
            a=b
            b=c

class Hybrid(b, c):
    def hybrid_sound(self):
        
        print("Hybrid makes a sound")
        print(self.n)

hybrid = Hybrid()
hybrid.prime()      # Inherited from a
hybrid.fact()       # Inherited from b
hybrid.feb()        # Inherited from c
hybrid.hybrid_sound()  # Method from Hybrid class
