class PriorityQueue:
    def __init__(self, capacity=1):
        self.heap_size = 0
        self.heap_capacity = capacity
        self.heap = []

    def is_empty(self):
        return self.heap_size == 0

    def get_size(self):
        return self.heap_size

    def peek(self):
        if self.heap is not None:
            return self.heap[0]

    def contains(self, value):
        for i in self.heap:
            if i == value:
                return True
        return False

    def poll(self):
        return self.remove(0)

    def add(self, element):
        self.heap_size += 1
        self.heap.append(element)
        self.swim(self.heap_size - 1)

    def swim(self, index_of_node):

        parent_index = (index_of_node - 1) // 2

        if not index_of_node == 0:
            while self.less(index_of_node, parent_index) and index_of_node > 0:
                self.swap(index_of_node, parent_index)
                index_of_node = parent_index
                parent_index = (index_of_node - 1) // 2

    def sink(self, index_of_node):

        left_child_index = 2 * index_of_node + 1
        right_child_index = 2 * index_of_node + 2
        index_of_smallest = left_child_index

        if right_child_index < self.heap_size and left_child_index < self.heap_size:

            if self.less(right_child_index, left_child_index) and right_child_index < self.heap_size:
                index_of_smallest = right_child_index

            while self.less(index_of_smallest, index_of_node):
                self.swap(index_of_node, index_of_smallest)
                self.sink(index_of_smallest)

    def less(self, node1_index, node2_index):
        node1 = self.heap[node1_index]
        node2 = self.heap[node2_index]

        return node1 - node2 < 0

    def swap(self, node1_index, node2_index):
        temp = self.heap[node1_index]
        self.heap[node1_index] = self.heap[node2_index]
        self.heap[node2_index] = temp

    def remove(self, element_index):
        if self.is_empty():
            return None

        self.swap(element_index, self.heap_size - 1)
        removed = self.heap[self.heap_size - 1]
        del self.heap[self.heap_size - 1]
        self.heap_size -= 1

        self.sink(element_index)

        self.swim(element_index)

        return removed


