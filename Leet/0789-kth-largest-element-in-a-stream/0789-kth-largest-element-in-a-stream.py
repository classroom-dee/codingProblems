class KthLargest:

    def __init__(self, k: int, nums: list[int]):
        self.kth_largest = KHeap(k, nums)

    def add(self, val: int) -> int:
        self.kth_largest.k_push(val)
        return self.kth_largest.get_root()

class KHeap:
    # min of the k elements is the root
    def __init__(self, k: int, arr: list=None):
        self.k = k
        self.arr = []
        if arr:
            for n in arr:
                self.k_push(n)

    def get_root(self):
        return self.arr[0] if self.arr else None
    
    def k_push(self, n: int):
        self.push(n)
        if len(self.arr) > self.k:
            self.pop_min()
    
    def push(self, n: int):
        self.arr.append(n)
        curr_idx = len(self.arr) - 1
        parent_idx = (curr_idx - 1) // 2

        # 'bubble up'
        while curr_idx > 0:
            parent_idx = (curr_idx - 1) // 2
            if self.arr[curr_idx] >= self.arr[parent_idx]:
                break
            else:
                curr = self.arr[curr_idx]
                parent = self.arr[parent_idx]
                self.arr[curr_idx] = parent
                self.arr[parent_idx] = curr
                curr_idx = parent_idx

    def pop_min(self):
        """
        Does not return anything!
        """
        if len(self.arr) == 0:
            return
        self.arr[0] = self.arr[-1]
        self.arr.pop()

        # 'bubble down'
        curr_idx = 0
        left_idx = curr_idx * 2 + 1
        right_idx = curr_idx * 2 + 2
        while left_idx < len(self.arr):
            if right_idx < len(self.arr): # both children exist
                if self.arr[left_idx] < self.arr[right_idx]:
                    if self.arr[curr_idx] > self.arr[left_idx]:
                        left = self.arr[left_idx]
                        curr = self.arr[curr_idx]
                        self.arr[left_idx] = curr
                        self.arr[curr_idx] = left
                        curr_idx = left_idx
                    else:
                        break
                else:
                    if self.arr[curr_idx] > self.arr[right_idx]:
                        right = self.arr[right_idx]
                        curr = self.arr[curr_idx]
                        self.arr[right_idx] = curr
                        self.arr[curr_idx] = right
                        curr_idx = right_idx
                    else:
                        break
            else: # only left exists
                if self.arr[curr_idx] > self.arr[left_idx]:
                    left = self.arr[left_idx]
                    curr = self.arr[curr_idx]
                    self.arr[left_idx] = curr
                    self.arr[curr_idx] = left
                    curr_idx = left_idx
                else:
                    break
            
            # update idxes
            left_idx = curr_idx * 2 + 1
            right_idx = curr_idx * 2 + 2


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)