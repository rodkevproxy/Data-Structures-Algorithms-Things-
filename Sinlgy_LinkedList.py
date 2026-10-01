# So in order to get this done we have a few tricks
    # Dummy node and creating a list node class 

class ListNode: 
    def __init__(self, val, next_node = None):
        self.val = val 
        self.next_node = next_node

class LinkedList: 


    def __init__(self): 
        #Dummy node 
        self.head = ListNode [-1] #This index does not really matter at this point 
        self.tail = self.head #This makes sure that the list is not empty

    def get(self, index: int) -> int: 
        curr = self.head.next
        i = 0 



        
        


        