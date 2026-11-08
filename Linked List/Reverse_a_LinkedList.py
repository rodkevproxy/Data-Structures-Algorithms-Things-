#Two pointers solution

class Solution: 
    def reverseList (self, head: Optionalp[ListNode]) -> Optional[ListNode]:
        prev, curr = None, head 
        while curr:
             nxt = curr.next 
             curr.next = prev 
             prev = curr 
             curr = nxt 
        return prev 

#Recuirsive solution 




        