'''
Binary Tree: Data structure in which each node has maximum 2 children.
Left is greater than the parent and Right is less than the parent.
Example:
parent(10)
      /\
left(5) Right(15)
'''


class BinaryTreeNode():
    def __init__(self, parent):
        self.left   = None
        self.right  = None
        self.parent = parent

    def __repr__(self):
        return "Current node: {}".format(self.parent)

    def append(self, child):
        if child.parent < self.parent:
            self.right = child
        else:
            self.left = child

    def depth_first_traversal(self):
        print(self)
        if self.left:
            self.left.depth_first_traversal()
        if self.right:
            self.right.depth_first_traversal()

    def breadth_first_traversal(self, nodes=None):
        nodes = [self]
        while nodes:
            current_node = nodes.pop(0)
            print(current_node)
            if current_node.left:
                nodes.append(current_node.left)
            if current_node.right:
                nodes.append(current_node.right)

    def breadth_first_traversal_with_generator(self):
        def generator(self):
            nodes = [self]
            while nodes:
                current_node = nodes.pop(0)
                if current_node.left:
                    nodes.extend([current_node.left])
                if current_node.right:
                    nodes.extend([current_node.right])
                yield current_node

        for node in generator(self):
            print(node)


def main():
    root = BinaryTreeNode(10)
    child1 = BinaryTreeNode(5)
    child2 = BinaryTreeNode(15)
    child3 = BinaryTreeNode(1)
    child4 = BinaryTreeNode(6)

    root.append(child1)
    root.append(child2)
    child1.append(child3)
    child1.append(child4)

    print('Depth first traversal:')
    root.depth_first_traversal()
    print('Breadth first traversal:')
    root.breadth_first_traversal()
    print('Breadth first traversal with generator:')
    root.breadth_first_traversal_with_generator()

if __name__ == "__main__":
    main()
