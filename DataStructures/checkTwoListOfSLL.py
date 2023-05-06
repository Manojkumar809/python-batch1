# checking the two given lists whether both are same or not
class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
class LinkedList:
    def __init__(self):
        self.head = None
        self.last_node = None
    def append(self, data):
        if (self.head == None):
            self.head = Node(data)
            self.last_node = self.head
        else:
            self.last_node.next = Node(data)
            self.last_node = self.last_node.next
        
def is_equal(list1,list2):
    temp1 = list1.head
    temp2 = list2.head
    while (temp1 and temp2):
        if (temp1.data != temp2.data):
            return False
        temp1 =  temp1.next
        temp2 =  temp2.next
    if (temp1 == None and temp2 == None):
        return True
    else:
        return False
list1,list2 = LinkedList(),LinkedList()
list1data = list(map(int, input('enter the elements in list1 : ').split()))
for data in list1data:
    list1.append(data)
list2data = list(map(int, input('enter the elements in list1 : ').split()))
for data in list2data:
    list2.append(data)
if is_equal(list1, list2):
    print('Both the given linked lists are same')
else:
    print('Both the given linked lists are not same')