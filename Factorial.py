# One-branch factoial 

# n! = n * (n-1) * (n-2) * ... 1
# 5! is the same as 5! = 5 x 4!
# Recursion is all about sub problems 

int factorial (int n) {
    if n <= 1 { 
        return 1
    }

    return n * factorial(n - 1)
}