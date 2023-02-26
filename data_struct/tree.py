class Node():
    def __init__(self, value) -> None:
        self.value = value
        self.childrens = []
    
    def add(self, value):
        self.childrens.append(value)
    
    def __str__(self) -> str:
        return self.value

class Tree():
    def __init__(self, value=None) -> None:
        self.root = Node(value)
        self.current = self.root
    
    def printTree(self, root: Node, level = 0) -> str:
          print("  " * level, root.value)
          for child in root.childrens:
            self.printTree(child, level+1)
    
    def add_node(self, value) -> None:
        n = Node(value)
        self.current.add(n)
    
    def navigate_to(self, value:Node) -> bool:
        nodes = [x for x in self.current.childrens if x.value == value]
        if len(nodes) >= 1:
            self.current = nodes[0]
            return True
        return False

    def reset(self) -> None:
        self.current = self.root