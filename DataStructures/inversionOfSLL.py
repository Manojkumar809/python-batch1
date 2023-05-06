# inversing or reversing the list
class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
class LinkedList:
    def __init__(self):
        self.head = None
    def insert_at_beg(self, data):
        newNode = Node(data)
        if (self.head == None):
            self.head = newNode
        else:
            newNode.next = self.head
            self.head = newNode
    def display(self):
        if (self.head == None):
            print('the linked list is  empty')
        else:
            temp = self.head
            while temp != None:
                print(temp.data, '=>', end='')
                temp = temp.next
        print()

obj = LinkedList()
for i in range(int(input('no of elements you would like to add : '))):
    data = int(input('enter the data of item : '))
    obj.insert_at_beg(data)
print('the linked list is : ', end='')
obj.display()