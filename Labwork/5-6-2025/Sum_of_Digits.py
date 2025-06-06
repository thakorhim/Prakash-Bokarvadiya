num = int(input("Enter a number: "))
count = 0
while num != 0:
    num //= 10
    count += 1
print("Number of digits: " + str(count))