import java.util.Stack;

public class stacks {
    public static void main(String[] args) {
        Stack<String> stack = new Stack<String>();

        //System.out.println(stack.empty()); This is how we check if a stack is empty 
        stack.push("Minecraft"); 
        stack.push("Doom"); 
        stack.push("Wardogs"); 
        stack.push("Any other game tbh"); 

        System.out.println(stack);

        stack.pop(); //This will remove the top object, when doing this proccess, if you just want to re-assing it can be done following these steps 
        //String popGame = stack.pop();  
        System.out.println(stack.peek()); //This will return the very first object of the stack 
        System.out.println(stack.search("Doom")); //This will return the position of that object tga 




        







 


        
        
    }
    
}
