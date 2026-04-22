class Node:
    def __init__(self, value):
        self.value = value
        self.children = []

    def add_child(self, child):
        self.children.append(child)

def dfs(start_node):
    stack = [start_node]   

    while stack:
        node = stack.pop()  
        print(node.value)

        for child in reversed(node.children):
            stack.append(child)


root = Node("A")
b = Node("B")
c = Node("C")
d = Node("D")
e = Node("E")
f = Node("F")

root.add_child(b)
root.add_child(c)
b.add_child(d)
b.add_child(e)
c.add_child(f)

dfs(root)