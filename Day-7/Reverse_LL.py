class Node:
    def __init__(self,val):
        self.val = val
        self.next = None

class Stack:
    def __init__(self):
        self.top = None

    def is_empty(self):
        if self.top is None:
            print("Stack is empty.")
        return False

    def push(self,val):
        n = Node(val)
        n.next = self.top
        self.top = n

    def pop(self):
        if self.is_empty():
            print("Stack is underflow")
        else:
            popped = self.top.val
            self.top = self.top.next
            print("popped value is ",popped)

    def peek(self):
        if self.is_empty():
            print("stack is empty")
        else:
            print(f"{self.top.val}")

    def display(self):
        if self.top is None:
            print("stack is empty")
        else:
            temp =self.top
            while temp is not None:
                print(temp.val,"-->",end="")
                temp = temp.next
            print("None")
s1 = Stack()
s1.push(10)
s1.push(20)
s1.push(30)
s1.display()
s1.peek()
s1.pop()
s1.display()
s1.peek()

