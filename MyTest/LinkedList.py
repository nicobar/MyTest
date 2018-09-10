class Node():
    
    def __init__(self, name=None):
        self.name=name
        self.next=None

class Linked_list():
    
    def __init__(self):
        self.head = None 
    
    def printlist(self):
        p = self.head
        while p is not None:
            print(p.name)
            p=p.next 
            
    def add_beginning(self, newname):
        
        NewNode=Node(newname)
        NewNode.next = self.head
        self.head = NewNode
        
    def add_end(self, newname):
        
        NewNode = Node(newname)
        if self.head is None:
            self.head = NewNode
            return
        p = self.head
        while(p.next):
            p = p.next
        p.next=NewNode
    
    def Remove_Node(self, Removekey):

        p = self.head

        if (p is not None):
            if (p.name == Removekey):
                self.head = p.next
                p = None
                return

        while (p is not None):
            if p.name == Removekey:
                break
            prev = p
            p = p.next

        if (p == None):
            return

        prev.next = p.next

        p = None

if __name__ == "__main__":
    
    L = Linked_list()
    L.head = Node("Mon")
    elem2 = Node("Tue")
    elem3 = Node("Wed")
    L.head.next=elem2
    elem2.next=elem3
    
    L.add_beginning("Sun")
    L.add_end("Thu")
    L.Remove_Node("Wed")
    L.printlist()
