#DYNAMIC ARRAY 

R#EPLACE ELEMENTS WITH GREATEST ELEMENT ON RIGHT SIDE 

#    - Imagine there is a -1 (last element has to be a -1)
#    - Compute the values in reversed order, becuase to get the new value at position 1 we need to know the value at position
#    2 and so on. 

#DESIGN A DYNAMIC ARRAY 

class DynamicArray:
    
    def __init__(self, capacity: int):
        self.capacity = capacity # Variable for the capacity since the array is dynamic and is going to be changing 
        self.size = 0 
        self.arr = [0] * 4 #This is how we initialize the capacity of the array


    def get(self, i: int) -> int:
        self.arr [i]

    def set(self, i: int, n: int) -> None:
        self.arr[i] = n 
        

    def pushback(self, n: int) -> None:
        self.capacity == self.size: 
            resize()
        self.arr[self.size] = n 
        self.size += 1 

    def popback(self) -> int:
        if self.size > 0: 
            self.size -= 1 
        #Soft deletion
        return self.arr[self.size]
 

    def resize(self) -> None:
        self.size = 2 * self.size 
        new_arr [0] * self.size 

        for i in range(self.size): 
            new_arr[i] = self.arr[i]
        self.arr = new_arr

    def getSize(self) -> int:
        return self.size 
    
    def getCapacity(self) -> int:
        return self.capacity 