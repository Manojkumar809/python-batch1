# Circular linked list
class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
class Createlist:
    def __init__(self):
        self.head = Node(None)
        self.tail = Node(None)
        self.head.next = self.tail
        self.tail.next = self.head
    def addNode(self,data):
        newNode = Node(data)
        if (self.head.data == None):
            self.head = newNode
            self.tail = newNode
            newNode.next = self.head
			
        else:
            self.tail.next = newNode
            self.tail = newNode
            self.tail.next = self.head

    def display(self):
            current = self.head
            if (self.head == None):
                print('the linked list is empty')
                return
            else:
                print('Nodes of the circular linked list : ')
                print(current.data, '-->')
                while (current.next != self.head):
                    current = current.next
                print(current.data, '=>', end =' ')
            print()
st = Createlist()
st.addNode(100)
st.addNode(200)
st.addNode(300)
st.addNode(400)
st.addNode(500)
print('the linked list is : ', end=' ')
st.display()