# Deletion of node of linked list at a given position
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
    def addNode(self,data):
        newNode = Node(data)
        if (self.head == None):
            self.head = newNode
            self.tail = newNode
        else:
            self.tail.next = newNode
            self.tail  = newNode
    def display(self):
        temp = self.head
        if (self.head == None):
            print('the linked list is  empty')
        else:
            while temp:
                print(temp.data, '=>', end='')
                temp = temp.next
        print()
    def deleteatpos(self,pos):
        temp = self.head.next
        prev = self.head
        for i in range(1, pos-1):
            temp = temp.next
            prev = prev.next
        print('deleting the node',temp.data, 'at position', pos)
        prev.next = temp.next
        temp.next = None

obj = LinkedList()
n1 = obj.addNode(100)
n2 = obj.addNode(200)
n3 = obj.addNode(300)
n4 = obj.addNode(400)
obj.display()
obj.deleteatpos(3)
obj.display()