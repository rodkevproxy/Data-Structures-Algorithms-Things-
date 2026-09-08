#Stack = LIFO data structure. Last-in, First-out 
#       Stores obkects into a sort of "Vertical tower"
#       Push() toadd to the top 
#       Pop() to remove from the top 

def main():
    stack = [] 
    stack.append("Minecraft")
    stack.append("Doom")
    stack.append("Fortnite")
    print(stack)

    stack.pop()
    print(stack)


if __name__ == '__main__': 
        main()





