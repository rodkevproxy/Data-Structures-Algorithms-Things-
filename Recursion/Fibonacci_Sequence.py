def fibonacci(n): 
    if n <= 1: 
        # Base case: n = 0 or 1 
        return n 

# To reach the base case we need to break it into sub problems  
# Recursive case: fib(n) = fib(n - 1) + fib(n - 2)
return fibonacci (n - 1) + fibonacci (n - 2) # Base case 
