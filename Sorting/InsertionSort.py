#Insertion Sort 
#Consider any array of 1 value to be sorted 
#Use iterave solution 

#Base code 

for i in arr: 
    j = i - 1
    while j > 0 and arr [j + 1] < arr[j]:
        tmp = arr[j + 1] 
        arr[j + 1] = arr[j]
        arr[j] = tmp 
    j -= 1 

    
        


   

