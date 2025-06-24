#palindrome
def palindrome(a):
    a=a.lower()
    a = str(a)
    if a == a[::-1]:
       print("Palindrome: ",a)
       
    else:
       print("Not Palindrome: ",a)

s=input("Enter a string: ")
print(palindrome(s))
