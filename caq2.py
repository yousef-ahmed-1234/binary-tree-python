class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def inorder_list(root, result):
    if root:
        inorder_list(root.left, result)
        result.append(root.value)
        inorder_list(root.right, result)


def is_bst(root):
    result = []
    inorder_list(root, result)
    return result == sorted(result)


# Build tree
root = Node(8)
root.left = Node(3)
root.right = Node(10)

root.left.left = Node(1)
root.left.right = Node(6)

root.left.right.left = Node(4)
root.left.right.right = Node(7)

root.right.right = Node(14)
root.right.right.left = Node(13)


# Run
values = []
inorder_list(root, values)

print("In-order traversal:", values)

if is_bst(root):
    print("The tree is a BST")
else:
    print("The tree is NOT a BST")