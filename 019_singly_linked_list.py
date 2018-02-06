class Node():
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList():
    def __init__(self):
        self.head = None

    def traverse(self):
        if self.head == None:
            print("None")
            return
        current = self.head
        while current:
            print(current.data)
            current = current.next

    def append(self, new_data):
        new_node = Node(new_data)

        if self.head == None:
            self.head = new_node
            return

        current = self.head
        while current.next != None:
            current = current.next
        current.next = new_node

    def prepend(self, new_data):
        new_node = Node(new_data)

        if self.head == None:
            self.head = new_node
            return

        temp_node = self.head
        self.head = new_node
        new_node.next = temp_node

    def insert_after(self, prev_node, new_data):
        current = self.head
        while current != prev_node:
            current = current.next
        new_node = Node(new_data)
        new_node.next = current.next
        current.next = new_node

def main():
    one = Node(1)
    two = Node(2)
    three = Node(3)
    linked_list = LinkedList()
    linked_list.head = one
    one.next = two
    two.next = three

    # Traverse the linked list
    # 1->2->3
    linked_list.traverse()
    print('==============')

    # append a node at the end of the list
    # 1->2->3->4
    linked_list.append(4)
    linked_list.traverse()
    print('==============')

    # prepend a node at the start of the list
    # 0->1->2->3->4
    linked_list.prepend(0)
    linked_list.traverse()
    print('==============')

    # 0->1->8->2->3->4
    linked_list.insert_after(linked_list.head.next, 8)
    linked_list.traverse()
    print('==============')

    # Create a new linked list using the methods
    # 1->2->5->10
    ll = LinkedList()
    ll.append(5)
    ll.append(10)
    ll.prepend(1)
    ll.insert_after(ll.head, 2)
    ll.traverse()


if __name__ == '__main__':
    main()
