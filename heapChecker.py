"""This program returns true if the given array is a binary heap, False otherwise."""

class HeapCheck:
    def __init__(self, arr):
        self.arr = arr

    def check(self):
        
        #checking if all the internal nodes are smaller than their children. Returns False if not.
        for i in range((len(self.arr)-2)//2+1):
            if self.arr[i*2+1]<self.arr[i] or self.arr[i*2+2]<self.arr[i]:
                return False
        
        return True

arr = [2, 3, 5, 9, 1, 7]
ch = HeapCheck(arr)

print(ch.check())
