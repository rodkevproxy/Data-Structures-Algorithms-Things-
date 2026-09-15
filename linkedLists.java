import java.util.LinkedList;

class linkedLists{ 
        public static void main(String[] args) {
                    //Linked list, singly and doubly (This one stores two addresses)
                    //It has a node to the next element, each node has a address. 
                    //LinkedList are bad at searching 

                    LinkedList<String> linkedList = new LinkedList<>(); 
                    /*
                    linkedList.push("A");
                    linkedList.push("B");
                    linkedList.push("C");
                    linkedList.push("D");
                    linkedList.push("E");
                     */

                    linkedList.offer("A");
                    linkedList.offer("B");
                    linkedList.offer("C");
                    linkedList.offer("D");
                    linkedList.offer("E"); //Offer can also be use to push new material into the linkedList 

                    
                    System.out.println(linkedList);


                    //To add we can use .add(index, "")
                    linkedList.add(3, "B");

                    //To remove we can use .pop() and remover("")
                    linkedList.remove("E");

                    //To return de index of an object that we are looking for we can use, this returns -1 when no index is found
                    System.out.println(linkedList.indexOf("F")); 

                    //Some more useful ones, these two add First and Last
                    linkedList.addFirst("0"); //Add a head
                    linkedList.addLast("9"); // Add a tail

                    //These two can print First and Last 
                    System.out.println(linkedList.peekFirst());
                    System.out.println(linkedList.peekLast());

                    //We can also remov the tail and head of a linkedList using a variable 
                    String first = linkedList.removeFirst();
                    String last = linkedList.removeLast();

                        




                    

                        


                


        }
}