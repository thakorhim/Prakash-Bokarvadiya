num = int(input("Enter a number: "))
pal = num
sum = 0
while num != 0:
    rem = num % 10
    sum = sum * 10 + rem
    num = num // 10
if pal == sum:
    print(pal, "is a palindrome number")
else:
    print(pal, "is not a palindrome number")