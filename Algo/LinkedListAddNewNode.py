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
    
    
    
    print("")
    print("inserting kyle after denver")
    print("")
    
    
    llist.printList()
    
