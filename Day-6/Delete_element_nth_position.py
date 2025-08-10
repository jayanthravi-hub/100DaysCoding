"""delete the nde with val"""

class Node:
    def __init__(self,val):
        self.val = val
        self.next = None

class LL:
    def __init__(self):
        self.root = None

    def addNode(self, val):
        n = Node(val)

        if self.root is None:
            self.root = n
            return
        else:
            temp = self.root
            while temp.next is not None:
                temp = temp.next
            temp.next = n

    def deleteNode(self,val):
        temp = self.root

        if temp is None:
            print("list is empty")
            return
        while temp and temp.val != val:
            temp = temp.next

        if temp == self.root:
            self.root = temp.next

            if self.root:
                self.root.next = None
    def display(self):
        if self.root is None:
            return
        else:
            temp = self.root
            while temp is not None:
                print(temp.val,"-->",end="")
                temp = temp.next
            print("None")
ll = LL()
ll.addNode(10)
ll.addNode(20)
ll.addNode(30)
ll.display()
