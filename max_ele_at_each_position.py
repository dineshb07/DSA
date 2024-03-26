class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    @staticmethod
    def insert(root, item):
        temp = Node(item)
        if root is None:
            root = temp
        else:
            ptr = root
            while ptr.next is not None:
                ptr = ptr.next
            ptr.next = temp
        return root

    @staticmethod
    def newlist(root1, root2):
        ptr1 = root1
        ptr2 = root2
        root = None
        while ptr1 is not None and ptr2 is not None:
            max_element = max(ptr1.data, ptr2.data)
            root = Node.insert(root, max_element)
            ptr1 = ptr1.next
            ptr2 = ptr2.next
        return root

    @staticmethod
    def display(root):
        while root is not None:
            print(root.data, end="")
            if root.next is not None:
                print("->", end="")
            root = root.next
        print()  # Print newline at the end


if __name__ == "__main__":
    root1 = None
    root2 = None
    root1 = Node.insert(root1, 4)
    root1 = Node.insert(root1, 5)
    root1 = Node.insert(root1, 2)
    print("first list:", end=" ")
    Node.display(root1)

    root2 = Node.insert(root2, 7)
    root2 = Node.insert(root2, 9)
    root2 = Node.insert(root2, 1)
    print("second list:", end=" ")
    Node.display(root2)

    root3 = Node.newlist(root1, root2)
    print("max element at each position merged list:", end=" ")
    Node.display(root3)
