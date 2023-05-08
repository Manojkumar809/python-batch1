# Search for the element in doubly linked list
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
    def search(self, value):
        if self.head == None:
            print('LL empty')
        else:
            temp = self.head
            while (temp):
                if temp.data == value:
                    print('searching for',temp.data, '....\n it is present')
                    break
                else:
                    temp = temp.next
                    if temp == None:
                        print('searching for',value, '....\n it is not present')


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
obj.search(400)
