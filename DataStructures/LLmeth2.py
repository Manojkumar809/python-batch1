# method - 2 for creating a node
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
class singlelinkedlist:
    def __init__(self):
        self.head = None
    def display(self):
        if self.head is None:
            print('the linked list is empty')
        else:
            temp = self.head
            while temp :
                print(temp.data, '=>', end='')
                temp = temp.next

obj = singlelinkedlist()
n = Node(10)
obj.head = n
n1 = Node(20)
obj.head.next = n1
n2 = Node(30)
n1.next = n2
n3 = Node(40) 
n2.next = n3
obj.display()            