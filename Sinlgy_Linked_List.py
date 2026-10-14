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
        curr = self.head.next #This is is pointing to head.next because of the dummy node 
        i = 0 
        while curr: 
            if i == index: 
                return curr.val 
            i += 1 
            curr = curr.next 
        return -1 # this handles the out of bounds case

    def insertHead(self, val: int) -> None:
        new_node = ListNode(val) #Take the given value and convert it into a new node 
        new_node.next = self.head.next 
        self.head.next = new_node 

        #If list was empty
        if not new_node.next:
            self.tail = new_node
        
        
        

    def insertTail(self, val: int) -> None:
     

    def remove(self, index: int) -> bool:

  
    def getValues(self) -> List[int]:
