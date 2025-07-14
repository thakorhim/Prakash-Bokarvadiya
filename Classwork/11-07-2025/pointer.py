class Myclass:
    def sum(self):
        a=10
        b=20
        print("a=",a)
        print("b=",b)
        self.c=a
        self.d=a
class Myclass2(Myclass):
    def sum(self):
        super().sum()
        d=self.c+self.d
        print("sum=",d)
obj=Myclass2()
obj.sum()