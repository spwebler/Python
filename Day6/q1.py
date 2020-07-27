test_keys = ["a", "b", "c","d","e"] 
test_values = [1,2,3,4,5,6,7,8] 
  
# Printing original keys-value lists 
print ("Original key list is : " + str(test_keys)) 
print ("Original value list is : " + str(test_values)) 
  
# using dictionary comprehension 
# to convert lists to dictionary 
res = {test_keys[i]: test_values[i] for i in range(len(test_keys))} 
  
# Printing resultant dictionary  
print ("Resultant dictionary is : " +  str(res)) 