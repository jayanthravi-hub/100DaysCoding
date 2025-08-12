class Node:
    def __init__(self,val):
        self.val = val
        self.next = None

class LinkedList:
    def __init__(self):
        self.root = None

    def addNode(self,val):
        n = Node(val)
        if self.root == None:
            self.root = n
        else:
            temp = self.root
            while temp.next is not None:
                temp = temp.next
            temp.next = n

    def delete_node(self,n):
        temp = Node(0)
        temp.next = self.root
        slow = temp
        fast = temp

        for i in range(n + 1):
            fast = fast.next

        while fast is not None:
            slow = slow.next
            fast = fast.next
        slow.next = slow.next.next

        self.root = temp.next
    def display(self):
        if self.root is None:
            return
        else:
            temp = self.root
            while temp is not None:
                print(temp.val,"-->",end="")
                temp = temp.next
            print("None")
LL = LinkedList()
LL.addNode(10)
LL.addNode(20)
LL.addNode(30)
LL.display()
LL.delete_node(2)
LL.display()
