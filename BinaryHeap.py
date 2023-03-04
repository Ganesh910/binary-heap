"""This program creates Binary Heap"""


class Heap:
    def __init__(self, arr):
        self.arr = arr
        self.nonLeaf = (len(arr)-2)//2 #index of last non-leaf node, leaf nodes start after that
        self.build_min_heap()

    def build_min_heap(self):

        #Heapifying all non-leaf nodes from last to first
        for i in range(self.nonLeaf, -1, -1):
            self.heapify(i)

    def heapify(self, index):
        child1 = index*2+1 #index of left child
        child2 = index*2+2 #Index of right child

        # Is parent larger than it's left child?
        if self.arr[index]>self.arr[child1]:

            # Checks if right child exists or not
            if child2>=len(self.arr):
                child2=child1
            
            #Is left child smaller than right child?
            if self.arr[child2]>=self.arr[child1]:

                # Then Swap them
                self.arr[index], self.arr[child1]=self.arr[child1], self.arr[index]

                # And then check recusively same thing on the child
                if child1<=self.nonLeaf:
                    self.heapify(child1)

            # If right child is even smaller than left, then swap parent with right child
            else:
                self.arr[index], self.arr[child2]=self.arr[child2], self.arr[index]

                # Then check recursively same thing on the child
                if child2<=self.nonLeaf:
                    self.heapify(child2)

    def minimum(self):
        if len(self.arr)!=0:
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
    # arr = [4, 1, 3, 2, 16, 9, 10, 14, 8, 7, 2, 4, 5, 7, 8, 4, 3]
    arr = [5, 3, 7, 9, 1, 2]
    heap = Heap(arr)
    print(arr)

if __name__=="__main__":
    main()