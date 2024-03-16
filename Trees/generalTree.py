class GeneralTree:
    def __init__(self, data):
        self.data = data
        self.children = []
        self.parent = None
        
        
    def add_child(self, child):
        child.parent = self
        self.children.append(child)
    
    
    def get_level(self):
        level = 0
        p = self.parent
        
        while p != None:
            #print(self.parent)
            
            level += 1
            p = p.parent
        
        return level
    
    def print_tree(self):
        spaces = " " * self.get_level() * 4
        prefix = spaces+ "|__" if self.parent else ""
        
        print(prefix + self.data)
        
        if self.children:
            for child in self.children:
                child.print_tree()


def build_electronic_tree():
    electronics = GeneralTree("Electronic")
    
    
    # creates tree with node as laptops
    laptops = GeneralTree("Laptops")
    
    # laptops leafs are different types of laptops
    laptops.add_child(GeneralTree("Mac"))
    laptops.add_child(GeneralTree("HP"))
    laptops.add_child(GeneralTree("ASUS"))
    
    
    #creates tree node of phones
    phones = GeneralTree("Phones")
    phones.add_child(GeneralTree("Iphone"))
    phones.add_child(GeneralTree("Samsung"))
    
    # add the laptops and phone nodes to root electronics
    electronics.add_child(laptops)
    electronics.add_child(phones)
    
    return electronics
   

if __name__ == '__main__':
    root = build_electronic_tree()
    root.print_tree()
    #print(root.get_level())