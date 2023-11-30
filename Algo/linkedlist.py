class Node:
    
    # Function to initialize the node object, our constructor.
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList():
    
    # Function prints contents of linked list
    def printList(self):
        temp = self.head
        while (temp):
            print (temp.data)
            temp = temp.next
            

    


if __name__ == "__main__":
    
    llist = LinkedList()
    
    llist.head = Node("Chicago")
    
    second = Node("Denver")
    
    llist.head.next = second # Link first node with second
    
    third = Node("Dallas")
    
    second.next = third # Linked second node with the third node
    
    llist.printList()
    
