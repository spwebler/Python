list1=[1,5,3,2,4]
list2=[7,10,8,6,9]
list3=list1+list2
list4=[]
for num in range(min(list3),max(list3)+1):
    if num in list3:
        list4.append(num)
print(list4)