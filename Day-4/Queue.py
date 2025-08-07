class Queue:
    def __init__(self,capacity):
        self.queue = [0]*capacity
        self.capacity = capacity
        self.front = 0
        self.rear = 0

    def is_empty(self):
        if self.front == self.rear:
            print("Queue is empty")

    def is_full(self):
        if self.rear == self.capacity:
            print("Queue is full")

    def enqueue(self, val):
        if self.is_full():
            print("Queue is full please try after sometime.")
        else:
            self.queue[self.rear] = val
            self.rear += 1
            print(f"{val} is enqueued")

    def dequeue(self):
        if self.is_empty():
            print("Queue is empty please try after some time")
        else:
            val = self.queue[self.front]
            self.front += 1
            print(f"{val} is dequeued")

    def peek(self):
        if self.is_empty():
            print("Queue is empty")
        else:
            print(self.queue[self.front])

    def display(self):
        if self.is_empty():
            print("Nothing to print your Queue is empty")
        else:
            for i in range(self.front,self.rear):
                print(self.queue[i],"-->",end='')
q1 = Queue(5)
q1.enqueue(10)
q1.enqueue(20)
q1.enqueue(30)
q1.display()
q1.peek()
q1.dequeue()
q1.display()
print()     # used to print in new line
q1.peek()

