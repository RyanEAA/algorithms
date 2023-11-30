# Assignment-10 – COSC 2316-01 – Professor McCurry
#  Implemented by - Ryan Aparicio

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
 
    def insertAfter(self, prev_node, new_data):
        
        #.1. chek if the given pre node exitst
        
        if prev_node is None:
            print("the given previous node my be in LInkiedLIst")
            return
            
        #2. create a new node 
        #3. put in the data
        new_node = Node(new_data)
        
        
        #4. make next of new node as next of prev_node
        new_node.next = prev_node.next
        
        #5. make next of prev_node as new_node
        prev_node.next = new_node
        
    def removeFirst(self):
        # Remove the first node in the linked list
        if self.head is not None:
            temp = self.head
            self.head = temp.next
            temp = None

    def removeLast(self):
        # Remove the last node in the linked list
        if self.head is None:
            return

        if self.head.next is None:
            self.head = None
            return

        temp = self.head
        while temp.next.next is not None:
            temp = temp.next

        temp.next = None

    def removeAt(self, key):
        # Remove the node with the given key from the linked list
        temp = self.head

        # If the key is in the head node
        if temp is not None and temp.data == key:
            self.head = temp.next
            temp = None
            return

        # Search for the key, keep track of the previous node
        prev = None
        while temp is not None and temp.data != key:
            prev = temp
            temp = temp.next

        # If key was not present in the linked list
        if temp is None:
            return

        # Unlink the node from the linked list
        prev.next = temp.next

        temp = None
        
        
        
            

if __name__ == "__main__":
    
    llist = LinkedList()
    
    llist.head = Node("San Jose")
    
    second = Node("Panama City")
    llist.head.next = second
    third = Node("San Pedro Sula")
    second.next = third
    fourth = Node("Tegucigalpa")
    third.next = fourth
    fifth = Node("Managua")
    fourth.next = fifth
    sixth = Node("San Salvador")
    fifth.next = sixth
    seventh = Node("Guatemala City")
    sixth.next = seventh
    eighth = Node("Belmopan")
    seventh.next = eighth
    ninth = Node("Mexico City")
    eighth.next = ninth

    
    print("printing initial linked list")
    llist.printList()
    print("")
    
    print("removing head node (San Jose)")
    llist.removeFirst()
    llist.printList()
    print("")
    

    
    print("removing last node, (Mexico City)")
    llist.removeLast()
    llist.printList()
    print("")
    
    print("removing Tegucigalpa node")
    llist.removeAt("Tegucigalpa")
    llist.printList()
    print("")
    
    