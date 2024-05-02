import random

class Node:
    def __init__(self, x):
        self.x = x
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.root = None

    def insert(self, val):
        if self.root is None:
            self.root = Node(val)
            return
        prev, cur = None, self.root
        while cur is not None:
            if val > cur.x:
                prev, cur = cur, cur.right
            else:
                prev, cur = cur, cur.left
        if val > prev.x:
            prev.right = Node(val)
        else:
            prev.left = Node(val)
        
    def search(self, root, val):
        cur = root
        while cur.x != val:
            if val > cur.x:
                cur = cur.right
            else:
                cur = cur.left
        return cur

    def search_with_prev(self, val):
        prev, cur = None, self.root
        while cur.x != val:
            if val > cur.x:
                prev, cur = cur, cur.right
            else:
                prev, cur = cur, cur.left
        return prev, cur

    def inorder_traversal(self):
        inorder_list = []
        visited = set()
        if not self.root:
            return []
        stack = [self.root]
        while stack:
            cur = stack[-1]
            if cur.left and cur.x not in visited:
                visited.add(cur.x)
                stack.append(cur.left)
            else:
                cur = stack.pop()
                inorder_list.append(cur.x)
                if cur.right:
                    stack.append(cur.right)
        return inorder_list

    def get_root(self):
        return self.root

    def delete(self, root, val):
        prev, cur = None, root
        while cur and val != cur.x:
            if cur.x < val:
                prev, cur = cur, cur.right
            else:
                prev, cur = cur, cur.left
        if not cur:
            return None
        
        # Leaf node
        if not cur.left and not cur.right:
            return self.delete_leaf(root, prev, cur)
        
        if not cur.left or not cur.right:
            return self.delete_single_child(root, prev, cur)
        
        return self.delete_two_child(cur)

    def delete_leaf(self, root, prev, cur):
        if not prev:
            root = None
            return cur
        if prev.left == cur:
            prev.left = None
        else:
            prev.right = None
        return cur


    def delete_single_child(self, root, prev, cur):
        node = cur.left if cur.left else cur.right
        if not prev:
            root = node
            return
        if prev.left == cur:
            prev.left = node
        else:
            prev.right = node
    
    def delete_two_child(self, cur):
        print(f'In delete two child {cur.x}')
        succ = self.successor(cur)
        cur.x = succ.x
        deleted_node = self.delete(cur.right, cur.x)
        if deleted_node == cur.right:
            cur.right = None
        return deleted_node

    def successor(self, node):
        if not node.right:
            return None
        succ = node.right
        while succ.left:
            succ = succ.left
        return succ

    def delete_node_with_one_child(self, prev, cur):
        node = cur.left if cur.left else cur.right
        if not prev:
            self.root = node
            return
        if prev.left == cur:
            prev.left = node
        else:
            prev.right = node




def permutation(n):
    v = list(range(1,n+1))
    random.shuffle(v)
    return v


bst = BST()
bst.insert(2)
bst.insert(1)
bst.insert(3)
root = bst.get_root()
n = bst.search(root, 2)
print(n.x, n.left.x, n.right.x)
print(bst.inorder_traversal())
bst.delete(bst.get_root(), 2)
print(bst.inorder_traversal())


test1 = permutation(10)
bst = BST()
for val in test1:
    bst.insert(val)
root = bst.get_root()
n = bst.search(root, 8)
#print(n.x, n.left.x, n.right.x)
print(bst.inorder_traversal())
bst.delete(bst.get_root(), 5)
print(bst.inorder_traversal())
bst.delete(bst.get_root(), 1)
print(bst.inorder_traversal())
bst.delete(bst.get_root(), 10)
print(bst.inorder_traversal())
