list=[]
x=int(input("enter the list length"))
for i in range(0,x):
    y=input("enter the names")
    list.append(y)
print(list)
count=0
for i in list:
    count+=i.lower().count("a")
print(count)    
