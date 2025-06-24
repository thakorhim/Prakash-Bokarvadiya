d={1:10,"a":"we",2:20,"b":"hello",3:30,"c":"hi"}
print(type(d)) #typecheck
print(d.keys())  #all keys show
print(d.values())  #all values show
print(d.items())  #all items show
print(d[1])  #accessing value using key
d.update({4:40})  #adding new key value pair
print(d)  #updated dictionary
d[4]="prakash"  #updating value of existing key
print(d)  #updated dictionary with new value
d.popitem()  #removing last item
print(d)  #dictionary after removing last item

t=(1,2,3,4,5)  #tuple

d1=dict.fromkeys(t,"prakash")  #creating dictionary from tuple with default value
print(d1)  #dictionary created from tuple