stack = []
while (True):
    print("* * * Press * * *\n1 to traverse\n2 to add element\n3 to delete element\n")
    choice = int(input())
    if choice == 1:
        if len(stack) == 0:
            print("Empty")
        else:
            for i in stack:
             print(i)
    elif choice == 2:
        print("Enter element\n")
        e = int(input())
        stack.append(e)
        print("ELEMENT ADDED")
    elif choice == 3:
        stack.pop()
        print("ELEMENT REMOVED")
    else:
        print("Error")


