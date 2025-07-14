class Myclass:
    def prime(self):
        n=5
        print("number is", n)
        for i in range(2,n):
            if n%i==0:
                print("Not a prime number")
            else:
                print("Prime number")
                break
class Myclass1(Myclass):
    
    def prime(self):
        super().prime()
        n=10
        print("number is", n)
        for i in range(2,n):
            if n%i==0:
                print("Not a prime number")
            else:
                print("Prime number")
                break
obj = Myclass1()
obj.prime()  # This will call the overridden method in Myclass1