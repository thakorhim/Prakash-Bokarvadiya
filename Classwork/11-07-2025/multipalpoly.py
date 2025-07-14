class Myclass:
    def patan(self):
        n=5
        for i in range(1,n+1):
            print("*"*i)
        super().patan()
class Myclass2:
    def patan(self):
        n=5
        for i in range(n,0,-1):
            print("*"*i)
class Myclass3(Myclass,Myclass2):
    def patan(self): 
        super().patan()      
        n=5
        for i in range(1,n+1):
            print(" " * (n - i) + "*" * (2 * i - 1))
            #print(" " * (n - i) + "*" * (2 * i - 1))
        for i in range(n-1,0,-1):
            print(" "*(n - i)+"*"*(2*i-1))
        for i in range (1,n+1):
            print(" "*(n-i)+"*"*i)
        for i in range (n-1,0,-1):
            print(" "*(n-i)+"*"*i)
            
        for i in range(1,n+1):
            for j in range(1,i+1):
                print(j,end="")
            print()

obj =Myclass3()
obj.patan()