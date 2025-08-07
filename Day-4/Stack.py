class Stack:
    def __init__(self,capacity):
        self.stack = [0] * capacity
        self.capacity = capacity
        self.top = 0

    def is_empty(self):
        if self.top == 0:
            print("stack is empty.")

    def is_full(self):
        if self.top == self.capacity:
            print("stack is full")

    def push(self, val):
        if self.is_full():
            print("Stack is already full please try after sometime!")
        else:
            self.stack[self.top] = val
            self.top += 1
            print(f"{val} is pushed")

    def pop(self):
        if self.is_empty():
            print("stack is empty try after sometime!")
        else:
            self.top -= 1
            val = self.stack[self.top]
            print(f"{val} is popped")
    def peek(self):
        if self.is_empty():
            print("stack is in underflow")
        else:
            print(self.stack[self.top-1])

    def display(self):
        for i in range(self.top-1,-1,-1):
            print(self.stack[i],"-->",end='')

s1 = Stack(5)
s1.push(10)
s1.push(20)
s1.push(30)
s1.display()
s1.peek()
s1.pop()
s1.display()
print()
s1.peek()
