#string to 3 later print in center 
def string_to_mid_3_later_print(a):
    if len(a)%2==0:
        print("Not possible")
    else:
        mid=(len(a)//2)
        return(a[mid-1:mid+2])

#main

s=input("Enter a string: ")
print(string_to_mid_3_later_print(s))