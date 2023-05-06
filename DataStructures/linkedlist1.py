'''linked lists are three types 1)singly linked lists 2)doubly linked lists 3)circular linked lists'''
#method - 1 to create a node and link b/w them
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
class LinkedList:
    def __init__(self):
        self.head = None
        self.last_node = None
    def append(self, data):
        if self.last_node is None:
            self.head = Node(data)
            self.last_node = self.head
        else:
            self.last_node.next = Node(data)
            self.last_node = self.last_node.next
    def display(self):
        current = self.head
        while current is not None:
            print(current.data, '=> ', end='')
            current=current.next

obj = LinkedList()
n = int(input('enter the no of elements you want to add: '))
for i in range(n):
    a = int(input('enter data of an item: '))
    obj.append(a)
print('the linked list is : ', end=' ')
obj.display()