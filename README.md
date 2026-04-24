# 🌳 Binary Tree Traversals & BST Check (Python)

## 📌 Overview

This project demonstrates fundamental Binary Tree operations in Python, including:

- In-order traversal  
- Pre-order traversal  
- Post-order traversal  
- Binary Search Tree (BST) validation  

It includes two main tasks:
1. Traversing a binary tree using DFS methods  
2. Checking if a binary tree is a valid BST using in-order traversal  

---

## 📂 Project Structure

binary-tree-project/
│
├── traversals.py        # Tree traversal implementations
├── bst_check.py         # BST validation
└── README.md            # Documentation

---

## 🌳 Question 1: Tree Traversals

### 📌 Tree Used

        10
       /  \
      5    15
     / \     \
    2   7     20

---

### 🔄 Traversal Outputs

In-order (Left → Root → Right):  
2 5 7 10 15 20  

Pre-order (Root → Left → Right):  
10 5 2 7 15 20  

Post-order (Left → Right → Root):  
2 7 5 20 15 10  

---

### 💻 Code

```python
class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


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
```

---

## 🌳 Question 2: BST Validation

### 📌 Idea

A Binary Tree is a BST if its in-order traversal is sorted.

---

### 📌 Tree Used

        8
       / \
      3   10
     / \    \
    1   6    14
       / \   /
      4   7 13

---

### 📊 Output

In-order traversal:  
[1, 3, 4, 6, 7, 8, 10, 13, 14]

Result:  
The tree is a BST

---

### 💻 Code

```python
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


values = []
inorder_list(root, values)

print("In-order traversal:", values)

if is_bst(root):
    print("The tree is a BST")
else:
    print("The tree is NOT a BST")
```

---

## 🧠 Key Concepts

- Binary Tree structure  
- DFS traversal methods  
- In-order, pre-order, post-order logic  
- BST validation using sorted traversal  

---

