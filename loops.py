print("Enter three subject marks")
sub=0
sum=0
while(sub<3):
    marks=int(input())
    sum=sum+marks
    sub=sub+1

print(sum)
if(sum>35):
    if(sum>65):
        print("great")
    elif(sum<65 and sum>49):
        print("ok")
else:
    print("fail")
