nodes = dict()

class Node:
    def __init__(self, name, leftName, rightName):
        self._name = name
        self._leftName = leftName
        self._rightName = rightName
    
    def pre_traversal(self):
        result = ''
        result += self._name
        if self._leftName != '.':
            result += nodes[self._leftName].pre_traversal()
        if self._rightName != '.':
            result += nodes[self._rightName].pre_traversal()
        return result
    
    def inorder_traversal(self):
        result = ''
        if self._leftName != '.':
            result += nodes[self._leftName].inorder_traversal()
        result += self._name
        if self._rightName != '.':
            result += nodes[self._rightName].inorder_traversal()
        return result

    def post_traversal(self):
        result = ''
        if self._leftName != '.':
            result += nodes[self._leftName].post_traversal()
        if self._rightName != '.':
            result += nodes[self._rightName].post_traversal()
        result += self._name
        return result

N = int(input())
# print(abc_to_idx)
for _ in range(N):
    name, leftName, rightName = input().split()
    node = Node(name, leftName, rightName)
    nodes[name] = node

print(nodes['A'].pre_traversal())
print(nodes['A'].inorder_traversal())
print(nodes['A'].post_traversal())