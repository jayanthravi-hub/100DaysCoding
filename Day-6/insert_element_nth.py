class Node:
    def __init__(self,val):
        self.val = val
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.root = None

    def addNode(self,val):
        n = Node(val)
        if self.root is None:
            self.root = n
            return
        else:
            temp = self.root
            while temp.next is not None:
                temp = temp.next
            temp.next = n

    def insert_node(self,pos,val):
        n = Node(val)
        temp = self.root

        count = 0

        while temp.next is not None and count < pos:
            temp = temp.next
            count += 1
        if self.root is None:
            print("it is out of range.")
            return
        n.next = temp.next
        temp.next = n
    def display(self):
        if self.root is None:
            return
        else:
            temp =self.root
            while temp is not None:
                print(temp.val,"-->",end='')
                temp = temp.next
            print("None")

SLL = SinglyLinkedList()
SLL.addNode(10)
SLL.addNode(20)
SLL.addNode(30)
SLL.display()
SLL.insert_node(1,25)
SLL.display()
