# One-branch factoial 

# n! = n * (n-1) * (n-2) * ... 1
# 5! is the same as 5! = 5 x 4!
# Recursion is all about sub problems 

def factorial (int n) {
    if n <= 1 { 
        return 1
    }

    return n * factorial(n - 1)
}

#Reverse a linked list USING FACTORIAL 

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head.next: 
            return None 

        newHead = head
        if head.next: 
            newHead = self.reverseList(head.next) #This reachs the base case 
            head.next.next = head
        head.next = None 
        return newHead 

#Thinka about this as unpause in reverse





    