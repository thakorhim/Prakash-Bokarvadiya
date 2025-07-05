# file=open("text1.txt","w+")
# file.write("Hello, World!")
# file.tell()  # Get the current position in the file
# file.seek(0)# Move the cursor to the beginning of the file
# print(file.read())
# file.close()

file=open("text1.txt","r+")
file.write("Hello, World!")
file.seek(0)  # Move the cursor to the beginning of the file
print(file.read())
file.close()