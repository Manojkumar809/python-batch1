# there are 3 methods of insertion in singly linked list 1)beginning  2)end  3)atposition
#   1)Beginnning, 2)end & 3)atposition/inbetween
# inserting a node with data 100  at beginning
# inserting a node with data 200  at end
# inserting a node with data 300  at a position - 3
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
class singlelinkedlist:
    def __init__(self):
        self.head = None
    def insertbeg(self, data):      #insert at beginning
        nb =  Node(data)
        nb.next = self.head
        self.head = nb
    def insertend(self,data):      #insert at beginning
        ne = Node(data)
        temp =  self.head
        while temp.next :
            temp = temp.next
        temp.next = ne
        ne.next = None
    def insertpos(self,pos,data):      #insert at position
        np = Node(data)
        temp = self.head
        for i in range(pos-1):
            temp = temp.next
        np.next =  temp.next
        temp.next = np
    def display(self):
        if self.head is None:
            print('the linked list is empty')
        else:
            temp = self.head
            while temp:
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
obj.insertbeg(100)
obj.insertend(200)
obj.insertpos(3, 300)
obj.display()  