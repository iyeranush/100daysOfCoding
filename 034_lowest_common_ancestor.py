"""
Lowest common ancestor:
Given a binary tree, find the lowest common ancestor for two given nodes


"""

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def path_to(self, x):
        return find_path(self, x, [self])

    def find_path(self, x, path):
        if self.data == x:
            path.append()
            return path
        elif self.left == None and self.right == None:
            path.pop()
            return path
        elif self.data


def lca(root, a, b):
    path_to_a = path_to(root, a)
    path_to_b = path_to(root, b)

    for i in range(len(path_to_a)):
        if path_to_a[i] != path_to_b[i]:
            return path_to_a[i-1]

