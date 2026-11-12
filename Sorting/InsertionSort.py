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
    # Stable vs unstable 

# NeetCode problem, insertion sort using key word lists 

class Soution:
    def insertionSort(self, pairs: List[Pair]) -> List[List[Pair]]:
        n = len(pairs)
        res = [] #This stores the intermidiate states 
        for i in range(n): 
            j = i - 1 #This is the pointer to the left of i which we use to campare 
            while j >= 0 and pairs[j].key > pairs[j + 1].key:
                pairs[j], pairs[j + 1] = pairs[j + 1], pairs[j] #This is how i can swap values in python 
                j -= 1
                res.append(pairs[:]) #This is how i can clone lists in python  
        return res









    
        


   

