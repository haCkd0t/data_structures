class stackList:
    class _node():
        __slots__ = '_data','_next'
        def __init__(self,_data,_next):
            self._data = _data
            self._next = _next
    def __init__(self):
        self._head = None
        self._size = 0

    def isEmpty(self):
        return self._size == 0

    def push(self,e):
        self._head = self._node(e,self._head)
        self._size = self._size+1
    def pop(self):
        if self.isEmpty():
            print("Can't add its empty!!!")
        value = self._head._data
        self._head = self._head._next
        self._size = self._size-1
        return  value
    def top(self):
        if self.isEmpty():
            print("Empty")
        return self._head._data
    def dis(self):
        temp = self._head
        while(temp):
            print(temp._data,end=" -->")
            temp = temp._next
        print()

ls = stackList()

while(True):
    print("* * * Press * * *\n1 to add element\n2 to pop element\n3 to print head of stack\n4 to check if the stack is empty or not\n5 to traverse stack\n")
    choice = int(input())
    if choice == 1:
        el = int(input())
        ls.push(el)
    elif choice == 2:
        if ls.isEmpty():
            print("Stack is Empty!!")
            continue
        print("POPPED ELEMENT: ",ls.pop())
    elif choice == 3:
        if ls.isEmpty():
            print("Stack is Empty!!")
            continue
        print("Head Value is: ",ls.top())
    elif choice == 4:
        print(ls.isEmpty())
    elif choice == 5:
        if ls.isEmpty():
            print("Empty!!")
            continue
        ls.dis()
    else:
        print("Wrong input!!!")