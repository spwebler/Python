l=['JAPAN','INDIA','SPAIN','RAM','SAM']
l.append('dd')
print(l)
l.pop(5)
print(l)
l.insert(2,"shra")
print(l)


//store application
print("Welcome to Store")
print("Choose any three option from our store:\n 1:Pizza 2:Sandwitch 3:Toast 4:Ran")
n=0
while(n<3):
    print("Your"+str(n+1)+"order",int(input()))
    n=n+1
print("How many you want")
count=int(input())

print("Your purchase:",count*5)
