# On a doubly linked list we have two pointer one for the next and one for the previous 
# First and last node is set to null 

# When adding a new node, this order is very important

# tail.next = newNode 
# newNode = tail 
# tail = tail.next

# Removing a node 

# node2 = tail.prev
# node2.next = null 
# tail = node2 

# Queues and Dequeuue

#Here is how you define a doubly linkedlist 

class Node: 
    def __init__(self, value): 
        self.value = value 
        self.next = null 
        self.prev = null

def append(self, value: int) -> None: 
    new_node = Node(value)
    last_node = self.tail.prev #The tail is not the last node 

    last_node.next = new_node
    new_node.prev = last_node  
    new_node.next = self.tail 
    self.tail.prev = new_node 

def pop(self) -> int: #Now i have to handle the case where i have to delete from the end
    if self.isEmpty(): 
        return -1 

    target_node = self.tail.prev 
    value = target_node.value
    prev_node = target_node.prev

    prev_node.next = self.tail 
    self.tail.prev = prev_node 

    return value 

def popleft(self) -> int: 
    if self.isEmpty(): 
        return -1 

    




    