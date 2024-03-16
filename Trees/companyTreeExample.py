class PositionTree:
    def __init__(self, name, title):
        self.name = name
        self.title = title
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
    
    def print_tree(self, cond):
        
        pos = ""
        if cond == "both":
            pos += f"{self.name} ({self.title})"
            
        elif cond == "name":
            pos += f"{self.name}"
        else:
            pos += f"{self.title}"
            
        spaces = " " * self.get_level() * 4
        prefix = spaces+ "|__" if self.parent else ""
        
        print(prefix + pos)
        
        if self.children:
            for child in self.children:
                child.print_tree(cond)


def build_electronic_tree():
    # ceo is the root node
    ceo = PositionTree("Nilupul", "CEO")
    
    
    # cto is a child node of ceo
    cto = PositionTree("Chinmay", "CTO")
    
    # itHead will be child node of cto
    ifHead = PositionTree("Vishna", "Infrastructure Head")
    
    # these are child nodes of itHead
    ifHead.add_child(PositionTree("Dhaval", "Cloud Manager"))
    ifHead.add_child(PositionTree("Abhijit", "App Manager"))
    
    
    #creates tree node of phones
    hr = PositionTree("Gel", "HR Head")
    hr.add_child(PositionTree("Peter", "Recruitment Manager"))
    hr.add_child(PositionTree("Waqas", "Policy Manager"))
    
    
    # adds the ifHead to CTO
    cto.add_child(ifHead)
    
    # add the cto and hr nodes back to ceo
    ceo.add_child(cto)
    ceo.add_child(hr)
    
    return ceo
   

if __name__ == '__main__':
    root = build_electronic_tree()
    root.print_tree("both")
    #print(root.get_level())