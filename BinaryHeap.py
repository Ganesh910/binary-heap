"""This program creates Binary Heap"""


class Heap:
    def __init__(self, arr):
        self.arr = arr
        # index of last non-leaf node, leaf nodes start after that
        self.nonLeaf = (len(arr)-2)//2
        self.build_min_heap()

    def build_min_heap(self):

        # Heapifying all non-leaf nodes from last to first
        for i in range(self.nonLeaf, -1, -1):
            self.heapify(i)

    def heapify(self, parent):

        if parent > self.nonLeaf:
            return

        child1 = parent*2+1  # index of left child
        child2 = parent*2+2  # Index of right child

        # Is parent larger than it's left child?
        if self.arr[parent] > self.arr[child1]:

            # Swaps the parent with the left child if right child does not exist
            if child2 >= len(self.arr):
                self.arr[parent], self.arr[child1] = self.arr[child1], self.arr[parent]
                self.heapify(child1)
                return

            # Is left child smaller than right child?
            elif self.arr[child2] < self.arr[child1]:

                # Then Swap them
                self.arr[parent], self.arr[child2] = self.arr[child2], self.arr[parent]

                # And then check recusively same thing on the child
                if child1 <= self.nonLeaf:
                    self.heapify(child2)
                    return
            else:
                self.arr[parent], self.arr[child1] = self.arr[child1], self.arr[parent]
                self.heapify(child1)
                return
                
        if child2 < len(self.arr) and self.arr[parent] > self.arr[child2]:
            self.arr[parent], self.arr[child2] = self.arr[child2], self.arr[parent]
            self.heapify(child2)
            return

    def minimum(self):
        if len(self.arr) != 0:
            return self.arr[0]
        return None

    def extract_min(self):
        self.arr[0], self.arr[-1] = self.arr[-1], self.arr[0]
        self.heapify(0)

    def delete_min(self):
        pass

    def insert(self, value):
        pass

    def decrease_key(self):
        pass


def main():
    arr = [4, 1, 3, 2, 16, 9, 10, 14, 8, 7, 2, 4, 5, 7, 8, 4]
    # arr = [5, 3, 7, 9, 1, 2]
    heap = Heap(arr)
    print(arr)


if __name__ == "__main__":
    main()
