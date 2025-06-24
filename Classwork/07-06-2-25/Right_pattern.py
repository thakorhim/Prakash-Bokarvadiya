#     *
#    **
#   ***
#  ****
# *****
# for i in range(1,6):
#     for j in range(1,6):
#         if j>=6-i:#1>=4
#             print("*",end="")
#         else:
#             print(" ",end="")
#     print()
i=1

while i<6:
    j=1
    while j<=6:
       if j>=6-i:#1>=4
           print("*",end="")
       else:
            print(" ",end="")
       j=j+1
    print()
   
    i=i+1
    