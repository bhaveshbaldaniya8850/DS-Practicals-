#Name: Bhavesh Baldaniya
#Roll No: 306

import random

random.seed(23)

class Node:
    def _init_(self, val):
            self.val = val
                    self.leftChild = None
                            self.rightChild = None

def insert(root, key):
    if root is None:
            return Node(key)
    else:
            if root.val == key:
                        return root
                                elif root.val < key:
                                            root.rightChild = insert(root.rightChild, key)
                                                    else:
                                                                root.leftChild = insert(root.leftChild, key)
    return root

def PrintInorder(root):
    if root:
            PrintInorder(root.leftChild)
                    print(root.val, end=" ")
                            PrintInorder(root.rightChild)

def printPreorder(root):
    if root:
            print(root.val, end=" ")
                    printPreorder(root.leftChild)
                            printPreorder(root.rightChild)

def printPostorder(root):
    if root:
            printPostorder(root.leftChild)
                    printPostorder(root.rightChild)
                            print(root.val, end=" ")

tree = Node(20)
for i in range(10):
    insert(tree, random.randint(2, 100))

if _name_ == "_main_":
    print("inorder")
        PrintInorder(tree)
            print("\n")
                print("preorder")
                    printPreorder(tree)
                        print("\n")
                            print("postorder")
                                printPostorder(tree)
