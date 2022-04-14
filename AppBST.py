from BinarySearchTreeDS.BinarySearchTree import BST

bst = BST()

bst.insert(12)
bst.insert(10)
bst.insert(-2)
bst.insert(1)

bst.travel()

bst.remove(10)

print("--------------")

bst.travel()
