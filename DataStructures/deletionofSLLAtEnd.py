# deletion of node at the end of linked list
class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
class LinkedList:
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
    def delete(self):
        temp = self.head.next
        prev = self.head
        while temp.next != None:
            temp = temp.next
            prev = prev.next
        prev.next = None

obj = LinkedList()
n1 =  Node(100)
obj.head = n1
n2 =  Node(200)
obj.head.next = n2
n3 =  Node(100)
n2.next = n3
n4 =  Node(200)
n3.next = n4
obj.display()
obj.delete()
obj.display()
