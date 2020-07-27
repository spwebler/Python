
str1 = "what we think we become;we are Python developers"

# initializing substring 
sub1 = "Geeks"

# printing original string 
print("The original string is : " + str1) 

# printing substring 
print("The substring to find : " + sub1) 

# using list comprehension + startswith() 
# All occurrences of substring in string 
res = [i for i in range(len(str1)) if str1.startswith(sub1, i)] 

# printing result 
print("The start indices of the substrings are : " + str(res)) 
