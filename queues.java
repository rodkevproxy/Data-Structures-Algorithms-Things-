// Queue = FiFo data structure. A collection designed for holding elements prior to procesing. Linear data structure 

// Add = Enqueue, offer()
// Remove = Dequeue, poll()

import java.util.LinkedList;
import java.util.Queue;

public class queues {
    public static void main(String[] args) {
    
        Queue<String> queue = new LinkedList<String>(); //Queue is an interface and not a class, we can not create an instance of an interface. We are creating a LinkedList because this class implements queues 
        queue.offer("Karen"); 
        queue.offer("Chad"); 
        queue.offer("Steve"); 
        queue.offer("Harold");
        System.out.println(queue);
        System.out.println(queue.peek());
        queue.poll(); 
        System.out.println(queue);
        
        /.
        



        
    }
}
