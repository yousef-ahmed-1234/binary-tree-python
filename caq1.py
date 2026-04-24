class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


# Traversals
def inorder(root):
    if root:
        inorder(root.left)
        print(root.value, end=" ")
        inorder(root.right)


def preorder(root):
    if root:
        print(root.value, end=" ")
        preorder(root.left)
        preorder(root.right)


def postorder(root):
    if root:
        postorder(root.left)
        postorder(root.right)
        print(root.value, end=" ")


# Build tree
root = Node(10)
root.left = Node(5)
root.right = Node(15)
root.left.left = Node(2)
root.left.right = Node(7)
root.right.right = Node(20)


print("In-order:")
inorder(root)

print("\nPre-order:")
preorder(root)

print("\nPost-order:")
postorder(root)
