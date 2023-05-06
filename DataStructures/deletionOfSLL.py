# Deleting first node till single linked list becomes empty
class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
class Deletestart:
    def __init__(self):
        self.head = None
        self.tail = None
    def addNode(self, data):
        newNode = Node(data)
        if self.head == None:
            self.head = newNode
            self.tail =  newNode
        else:
            self.tail.next = newNode
            self.tail = newNode
    def DeleteFromStart(self):
        if (self.head == None):
            print('the linked list is empty')
            return
        else:
            if (self.head != self.tail):
                self.head = self.head.next
            else:
                self.head = self.tail = None
    def display(self):
        temp = self.head
        if (self.head == None):
            print('the linked list is empty')
        while temp!=None:
            print(temp.data, '=>', end='')
            temp = temp.next
        print()

obj = Deletestart()
obj.addNode(100)
obj.addNode(200)
obj.addNode(300)
obj.addNode(400)
print('the linked list is :', end='')
obj.display()
while (obj.head != None):
    obj.DeleteFromStart()
    print('the linked list is :', end='')
    obj.display()

            