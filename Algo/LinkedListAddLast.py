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
            
    def push(self, new_data):
        #1 and 2: allocate the node 
        # and put in the data
        new_node = Node(new_data)
        
        
        
        #3. make next of the new Node as head
        new_node.next = self.head # type: ignore
        
        
        #4. move the head to point to new node
        self.head = new_node
        
    
    def append(self, new_data):
        #1 create new node
        #2. put in the data
        #3. set next as None
        new_node = Node(new_data)
        
        
        #4. if the linked list is empty, then make the
        #new node as head
        
        if self.head is None:
            self.head = new_node
            return
        
        #5. Else traverse till the last node
        last = self.head
        while (last.next):
            last = last.next
            
        #6. Change the next of last node
        last.next = new_node # type: ignore
 
        
            

if __name__ == "__main__":
    
    llist = LinkedList()
    
    llist.head = Node("Chicago")
    
    second = Node("Denver")
    
    llist.head.next = second # type: ignore # Link first node with second
    
    third = Node("Dallas")
    
    second.next = third # type: ignore # Linked second node with the third node
    
    llist.printList()
    
    
    print("")
    print("adding los angeles to the head of the lsit")
    print("")
    llist.push("Los Angeles")
    
    print("")
    print("adding austin to the end of the list")
    llist.append("Austin")
    
    
    print("")
    print("adding seattle to the end of the list")
    print("")
    
    llist.append("Seattle")
    
    
    llist.printList()
    
