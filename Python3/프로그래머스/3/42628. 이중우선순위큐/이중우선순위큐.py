import heapq

class ToolMixin:
    def input_cleaner(self, stuff):
        """Casts input to int"""
        if isinstance(stuff, str):
            return int(stuff)
        elif isinstance(stuff, int):
            return stuff
        else:
            raise Exception("Uh No")

class DualPriorityQueue(ToolMixin):
    def __init__(self):
        self.mnh = []  
        self.mxh = []  
        self.rec = {}  # tracks valid elements

    def add(self, priority):
        priority = self.input_cleaner(priority)
        heapq.heappush(self.mnh, priority)
        heapq.heappush(self.mxh, -priority)
        self.rec[priority] = self.rec.get(priority, 0) + 1

    def pop(self, min_max):
        """:param min_max: '1' or '-1'"""
        min_max = self.input_cleaner(min_max)
        while self.mxh and self.rec:
            priority = (-1 * min_max) * heapq.heappop(self.mxh if min_max == 1 else self.mnh)
            if self.rec.get(priority, 0) > 0:
                self.rec[priority] -= 1
                if self.rec[priority] == 0:
                    del self.rec[priority]
                break
    
    def get_rec(self):
        if not self.rec:
            return [0, 0]
        else:
            # get max min
            while self.mxh and -self.mxh[0] not in self.rec:
                heapq.heappop(self.mxh)
            while self.mnh and self.mnh[0] not in self.rec:
                heapq.heappop(self.mnh)
            
            mx = -self.mxh[0] if self.mxh else 0
            mn = self.mnh[0] if self.mnh else 0

            return [mx, mn]

def solution(operations):
    dpq = DualPriorityQueue()
    for op in operations:
        inst = op.split()
        if inst[0] == "I": # add
            dpq.add(inst[1])
        else:
            dpq.pop(inst[1])
    return dpq.get_rec()