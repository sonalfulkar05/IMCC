# BST using Linked List
class Node:
    def __init__(self, value):
        self.left = None
        self.data = value
        self.right = None


class BST:
    def __init__(self):
        self.root = None
        self.cnt = 0  # Initialize node counter

    def insert(self, new_node):
        if self.root is None:  # BST is empty
            self.root = new_node
            self.cnt += 1
        else:
            temp = self.root
            while True:
                if new_node.data < temp.data:  # Left subtree
                    if temp.left is None:
                        temp.left = new_node
                        self.cnt += 1
                        return
                    else:
                        temp = temp.left
                else:  # Right subtree
                    if temp.right is None:
                        temp.right = new_node
                        self.cnt += 1
                        return
                    else:
                        temp = temp.right

    def inorder(self, rt):
        if rt is None:
            return
        self.inorder(rt.left)
        print(rt.data, end=" ")
        self.inorder(rt.right)

    def preorder(self, rt):
        if rt is None:
            return
        print(rt.data, end=" ")
        self.preorder(rt.left)
        self.preorder(rt.right)

    def postorder(self, rt):
        if rt is None:
            return
        self.postorder(rt.left)
        self.postorder(rt.right)
        print(rt.data, end=" ")

    def findminmax(self):
        if self.root is None:  # Guard against empty tree
            print("\nTree is empty")
            return

        temp = self.root
        while temp.left:
            temp = temp.left
        print("\nMin:", temp.data)

        temp = self.root
        while temp.right:
            temp = temp.right
        print("Max:", temp.data)
    def count_leaf_nodes(self, root):
        if root is None:
            return 0
        if root.left is None and root.right is None:
            return 1
        return self.count_leaf_nodes(root.left) + self.count_leaf_nodes(root.right)
    def count_nonleaf_nodes(self, root):
        if root is None:
            return 0
        if root.left is None and root.right is None:
            return 0
        return 1 + self.count_nonleaf_nodes(root.left) + self.count_nonleaf_nodes(root.right)
    # def del_node(self, rt, val):
    #     if rt is None:
    #         return rt
    #     if val < rt.data:
    #         rt.left = self.del_node(rt.left, val)
    #     elif val < rt.data:
    #         rt.right = self.del_node(rt.right, val)
    #     else:
    #         if rt.left is None: # node with right child only
    #             return rt.right
    #         if root.right is None: # node with left child only
    #             return rt.left
    #         #node has both left and right children
    #         succ = self.get_successor(rt)
    #         rt.data = succ.data
    #         rt.right = self.del_node(rt.right, succ.data)
    #         return rt
    # def get_successor(self, temp):
    #     temp = temp.right
    #     while temp.left is  not None:
    #         temp = temp.left
    #     return temp
    def del_node(self, rt, val):
        if rt is None:
            return rt
        if val < rt.data:
            rt.left = self.del_node(rt.left, val)
        elif val > rt.data:
            rt.right = self.del_node(rt.right, val)
        else:
            # Node with only one child or no child
            if rt.left is None:
                return rt.right
            elif rt.right is None:
                return rt.left

            # Node with two children: Get the inorder successor (smallest in the right subtree)
            succ = self.get_successor(rt)
            rt.data = succ.data  # Copy the inorder successor's content to this node
            rt.right = self.del_node(rt.right, succ.data)  # Delete the inorder successor

        return rt
    def get_successor(self, temp):
        temp = temp.right
        while temp.left is not None:
            temp = temp.left
        return temp
    def search(self, rt, val):
        if rt is None:
            return False
        if val == rt.data:
            return True
        elif val < rt.data:
            return self.search(rt.left, val)
        else:
            return self.search(rt.right, val)        
# Driver code
b1 = BST()
b1.insert(Node(100))
b1.insert(Node(10))
b1.insert(Node(450))
b1.insert(Node(0))
b1.insert(Node(65))
b1.insert(Node(300))

print("\nInorder:")
b1.inorder(b1.root)
print("\nNo of nodes:", b1.cnt)

print("\nPreorder:")
b1.preorder(b1.root)

print("\nPostorder:")
b1.postorder(b1.root)

b1.findminmax()
print("\nLeaf nodes:", b1.count_leaf_nodes(b1.root))
print("Non-leaf nodes:", b1.count_nonleaf_nodes(b1.root))
print("before deletion:", end=" ")
b1.inorder(b1.root)
b1.del_node(b1.root,10)
print("\nafter deletion:",end=" ")
b1.inorder(b1.root)
print("\nSearching for 65:", b1.search(b1.root, 65))