
def Merge(list1, list2): 
    final_list = list1 + list2 
    final_list.sort() 
    return(final_list) 
  

list1 = [10,20,40,60,70,80] 
list2 = [5,15,25,35,45,60] 
print(Merge(list1, list2)) 