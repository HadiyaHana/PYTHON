list=[]
n=int(input("Enter the list"))
for i in range(0,n):
    num=int(input("value"))
    list.append(num)
print(list)
for i in range(0,n):
    if list[i]>100:
        list[i]="over"
print(list)
    
   
