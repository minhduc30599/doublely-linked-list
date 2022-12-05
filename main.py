class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class DoubleLinkedList:
    def __init__(self):
        self.head = None

    def unshift(self, data):
        new_node = Node(data)
        new_node.next = self.head

        if self.head is not None:
            self.head.prev = new_node

        self.head = new_node
        new_node.prev = None

    def push(self, data):
        head = self.head

        if head is None:
            self.unshift(data)

        while head.next is not None:
            head = head.next

        new_node = Node(data)
        new_node.next = head.next
        head.next = new_node
        new_node.prev = head

    def insertBefore(self, data, key):
        head = self.head

        if head is None:
            self.unshift(data)

        new_node = Node(data)

        while head != key:
            head = head.next

            if head is None:
                print('Do not found key in the double linked list')
                break

    def insertAfter(self, data, key):
        head = self.head

        if head is None:
            self.unshift(data)

        new_node = Node(data)

        while head != key:
            head = head.next

            if head is None:
                print('Do not found key in the double linked list')
                break

        new_node.next = head.next
        new_node.prev = head
        head.next = new_node

        if head.next is not None:
            new_node.next.prev = new_node

    def printDll(self):
        head = self.head

        if head is None:
            print('Empty double linked list')

        while head is not None:
            print(f'Data: {head.data}')

            if head.next is not None:
                head = head.next
            else:
                break


if __name__ == '__main__':
    dll = DoubleLinkedList()
    dll.unshift(3)
    dll.unshift(2)
    dll.unshift(1)
    dll.insertAfter(5, dll.head)
    dll.push(7)
    dll.printDll()
