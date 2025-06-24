#uper side of tringal
#     *
#    * *    
#   * * *
#  * * * *
# * * * * *

for i in range(1,6):#2
    for j in range(1,i+1):#2     1     
        print(" ",end=" ")
        if j>=6-i:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
    