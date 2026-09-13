import java.util.*; 

public class priorityQueues {
    
    public static void main(String[] args) {
         //Priory Queue = A FIFO data structure that serves elements 
         //                with the highest priorities first 
         //                  before elements with lower priority

         Queue<Double> queue = new LinkedList<>();
         
         queue.offer(3.3);
         queue.offer(2.3);
         queue.offer(3.9);
         queue.offer(3.0);

         while(!queue.isEmpty()){ 
            System.out.println(queue.poll());
            
         }
    }
    
}
