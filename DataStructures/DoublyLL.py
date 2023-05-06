# Doubly linked list implementation or creation of doubly linked list
class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None
class doubleLinkedList:
    def __init__(self):
        self.head = None
    def display(self):
        if (self.head == None):
            print('the linked list is empty')
        else:
            temp = self.head
            while temp:
                print(temp.data, '=>', end='')
                temp = temp.next
        print()

obj = doubleLinkedList()
n1 = Node(100)
obj.head = n1
n2 = Node(200)
obj.head.next = n2
n2.prev = n1
n3 = Node(300)
n2.next = n3
n3.prev = n2
obj.display()
