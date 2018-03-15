"""
Given a binary search tree, find the sum of all the nodes in a given range.
Assume all nodes in the tree are integers.
range(a, b), where a <= node < b
return: sum

Eg.     20
    10       30
5      15  25    35
range(20, 31) => sum = 20 + 25 + 30

What do we know?
- Its a binary search tree
- Which means it has left, right node max 2 child nodes.
- left <= node < right
- recursion
time: O(log n) height of the tree
Pre-order traversal because we want to check root first.
"""

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def sum_nodes_in_range(root, a, b):
    total_sum = 0
    return sum_nodes_recursive(root, a, b, total_sum)

def sum_nodes_recursive(root, a, b, total_sum):
    if root == None:
        return total_sum
    if a <= root.data  and root.data < b:
        total_sum += root.data
        total_sum = sum_nodes_recursive(root.left, a, b, total_sum)
    total_sum = sum_nodes_recursive(root.right, a, b, total_sum)
    return total_sum
    """
        20
    10      30
    range(20, 30)
    sum_nodes_recursive(20, 20, 30, 0)
    sum_nodes_recursive(10, 20, 30, 20)
    sum_nodes_recursive(30, 20, 30, 20)
    return 50
    """
n1 = Node(10)
nl = Node(5)
nr = Node(30)
n1.left = nl
n1.right = nr
assert sum_nodes_in_range(n1, 20, 31) == 30

n1 = Node(20)
nl = Node(10)
nr = Node(30)
n1.left = nl
n1.right = nr
assert sum_nodes_in_range(n1, 20, 31) == 50
