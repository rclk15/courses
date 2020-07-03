"""
Ricky Cheah
4/12/2020

This driver file demonstrates the rebalance() method from the LinkedBST class. 

"""

from linkedbst import LinkedBST
import random

def main():
    
    # this section shows the rebalance() method.
    lyst = list(range(1,16))
#    lyst = ["A","B","C","D","E","F","G"]
    random.shuffle(lyst)
    tree1 = LinkedBST(lyst)
    print("Original unbalanced BST:")
    print(tree1)
    tree1.rebalance()
    print("BST after rebalance():")
    print(tree1)
    
    
    # this sections shows the various traversal methods.
    inorderList = list(tree1.inorder())
    print("Inorder", inorderList)
    preorderList = list(tree1.preorder())
    print("Preorder", preorderList)
    postorderList = list(tree1.postorder())
    print("Postorder", postorderList)
    levelorderList = list(tree1.levelorder())
    print("Levelorder", levelorderList)

if __name__ == "__main__":
    main()


