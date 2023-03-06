"""This program returns true if the given array is a binary heap, False otherwise."""

class HeapCheck:
    def __init__(self, arr):
        self.arr = arr

    def check(self):
        
        #checking if all the internal nodes are smaller than their children. Returns False if not.
        for i in range((len(self.arr)-2)//2+1):

            #if left child is smaller than parent or right child exists and smaller than parent
            if self.arr[i*2+1]<self.arr[i] or (i*2+2 < len(self.arr) and self.arr[i*2+2]<self.arr[i]):
                return False
        
        return True

arr = [1, 2, 3, 4, 2, 4, 7, 4, 8, 7, 16, 9, 5, 10, 8, 14]
ch = HeapCheck(arr)

print(ch.check())
