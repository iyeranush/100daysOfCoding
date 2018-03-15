"""
Note: This is a very naive solution. And an incorrect one.
Will post the correct one soon.
"""

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def insert(self, value):
        if self == None:
            self = value
        elif self.data >= value.data:
            if self.left == None:
                self.left = value
            else:
                self.left.insert(value)
        else:
            if self.right == None:
                self.right = value
            else:
                self.right.insert(value)

    def is_binary_search_tree(self):
        if self == None:
            return True

        if self.left:
            if self.left.data <= self.data:
                self.left.is_binary_search_tree()
            else:
                return False
        if self.right:
            if self.right.data > self.data:
                self.left.is_binary_search_tree()
            else:
                return False

        return True


def main():
    binary_tree = Node(10)
    binary_tree.insert(Node(5))
    binary_tree.insert(Node(15))
    binary_tree.insert(Node(1))
    binary_tree.insert(Node(7))
    binary_tree.insert(Node(14))
    binary_tree.insert(Node(20))

    print(binary_tree.is_binary_search_tree())

if __name__ == '__main__':
    main()
