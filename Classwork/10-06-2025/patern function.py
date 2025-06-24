#patterns function
def pattern1():
    for i in range(1,5):
        for j in range(1,i+1):
            print(j,end=" ")
        print()


#* pattern
def pattern2():
    for i in range(1,5):
        for j in range(1,i+1):
            print("*",end=" ")
        print()

print("pattern 1")
pattern1()
print("pattern 2")
pattern2()