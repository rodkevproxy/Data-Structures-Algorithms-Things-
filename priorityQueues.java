import java.util.*; 

public class priorityQueues {
    
    public static void main(String[] args) {
         //Priory Queue = A FIFO data structure that serves elements 
         //                with the highest priorities first 
         //                  before elements with lower priority

         Queue<Double> queue = new PriorityQueue<>(Collections.reverseOrder()); // Using this class will return an ordered elements in ascending order 
                                                      // Using the Collection method will allow us to reverse the output 
         queue.offer(3.3);
         queue.offer(2.3);
         queue.offer(3.9);
         queue.offer(3.0);

         while(!queue.isEmpty()){ 
            System.out.println(queue.poll());

         }
    }
    
}
