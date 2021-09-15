class DoublyLinkedList:
    def __init__(self):
        self.size = 0
        self.head = None
        self.tail = None

    class Node:
        def __init__(self, content, prev, following):
            self.content = content
            self.prev = prev
            self.following = following

        def __repr__(self):
            return str(self.content)

    def get_size(self):
        return self.size

    def is_empty(self):
        return self.get_size() == 0

    def add_to_start(self, element):
        if self.is_empty():
            self.head = self.tail = self.Node(element, None, None)
        else:
            self.head.prev = self.Node(element, None, self.head)
            self.head = self.head.prev

        self.size += 1

    def add_to_end(self, element):
        if self.is_empty():
            self.head = self.tail = self.Node(element, None, None)
        else:
            self.tail.following = self.Node(element, self.tail, None)
            self.tail = self.tail.following

        self.size += 1

    def peek_head(self):
        if not self.is_empty():
            return self.head.content

    def peek_tail(self):
        if not self.is_empty():
            return self.tail.content

    def delete_head(self):
        if not self.is_empty():
            content = self.head.content
            if self.head.following is not None:
                self.head = self.head.following
                self.size -= 1
            else:
                self.head = None
                self.tail = None
                self.size = 0

            return content

    def delete_tail(self):
        if not self.is_empty():
            content = self.tail.content
            if self.tail.prev is not None:
                self.tail = self.tail.prev
                self.size -= 1
            else:
                self.head = None
                self.tail = None
                self.size = 0

            return content

    def remove_node(self, node):
        if node.prev is None:
            return self.delete_head()
        if node.following is None:
            return self.delete_tail()

        node.following.prev = node.prev
        node.prev.following = node.following

        data = node.content

        self.size -= 1

        return data

    def remove_at_index(self, index):
        if not index < 0 or index >= self.size:
            if index < self.size/2:
                trav = self.head
                for i in range(index + 1):
                    trav = trav.following

            else:
                trav = self.tail
                for i in range(-(index + 1)):
                    trav = trav.prev

            return self.remove_node(trav)

    def remove_value(self, value):
        starting_size = self.size
        trav = self.head
        for i in range(self.size):
            trav = trav.following
            if trav.content == value:
                self.remove_node(trav)

        if self.size < starting_size:
            return True

        return False

    def index(self, value):
        index = -1
        trav = self.head
        for i in range(self.size):
            if trav.content == value:
                return index

            trav = trav.following
            index += 1

        return False

    def contains(self, value):
        trav = self.head
        for i in range(self.size):
            if trav.content == value:
                return True

            trav = trav.following

        return False