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

    def contains(self, value):
        if self.data == value:
            print(True)
        elif self.data > value:
            if self.left == None:
                print(False)
            else:
                self.left.contains(value)
        else:
            if self.right == None:
                print(False)
            else:
                self.right.contains(value)

    def print_in_order(self):
        # prints left -> root -> right
        if self.left:
            self.left.print_in_order()
        if self.data:
            print(self.data)
        if self.right:
            self.right.print_in_order()

    def print_pre_order(self):
        # prints root -> left -> right
        if self.data:
            print(self.data)
        if self.left:
            self.left.print_pre_order()
        if self.right:
            self.right.print_pre_order()

    def print_post_order(self):
        # prints left -> right -> root
        if self.left:
            self.left.print_pre_order()
        if self.right:
            self.right.print_pre_order()
        if self.data:
            print(self.data)


def main():
    binary_tree = Node(10)
    binary_tree.insert(Node(5))
    binary_tree.insert(Node(15))
    binary_tree.insert(Node(1))
    binary_tree.insert(Node(7))
    binary_tree.insert(Node(14))
    binary_tree.insert(Node(20))

    print("Does the binary tree contain 20?")
    binary_tree.contains(20)

    print('Print in order:')
    binary_tree.print_in_order()
    print('Print pre order:')
    binary_tree.print_pre_order()
    print('Print post order:')
    binary_tree.print_post_order()


if __name__ == '__main__':
    main()
