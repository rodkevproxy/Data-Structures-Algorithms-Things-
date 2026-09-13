import java.util.*; 

public class priorityQueues {
    
    public static void main(String[] args) {
         //Priory Queue = A FIFO data structure that serves elements 
         //                with the highest priorities first 
         //                  before elements with lower priority

         Queue<String> queue = new PriorityQueue<>(Collections.reverseOrder()); // Using this class will return an ordered elements in ascending order 
                                                      // Using the Collection method will allow us to reverse the output 
                                                      // As shown above this also works with strings sroting 
         queue.offer("B");
         queue.offer("A");
         queue.offer("D");
         queue.offer("B");

         while(!queue.isEmpty()){ 
            System.out.println(queue.poll());

         }
    }
    
}
