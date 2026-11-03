class LRUCache:

    def __init__(self, capacity: int):
        if capacity <= 0:
            raise ValueError("capacity should be positive")
        self.capacity = capacity
        self.lead = None
        self.tail = None
        self.cache = {}

    def mark_recent(self, key):
        if self.cache[key] is self.tail:
            return
        elif self.cache[key] is self.lead:
            nxt = self.cache[key].next
            nxt.prev = None
            self.lead = nxt
            self.tail.next = self.cache[key]
            self.cache[key].prev = self.tail
            self.cache[key].next = None
            self.tail = self.cache[key]
        else:  
            nxt = self.cache[key].next
            prv = self.cache[key].prev
            prv.next = nxt
            nxt.prev = prv
            self.tail.next = self.cache[key]
            self.cache[key].prev = self.tail
            self.cache[key].next = None
            self.tail = self.cache[key]

    def get(self, key: int) -> int:
        if not key in self.cache:
            return -1
        self.mark_recent(key)
        return self.cache[key].value

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.cache[key].value = value
            self.mark_recent(key)
            return
        if len(self.cache) == self.capacity:
            # evict
            self.cache.pop(self.lead.key)
            self.lead = self.lead.next
            if self.lead:
                self.lead.prev = None
            else:
                self.tail = None
            
            if not self.cache:
                self.lead = Things(key, value)
                self.tail = self.lead
                self.cache[key] = self.lead
            else:
                self.tail.next = Things(key, value)
                self.cache[key] = self.tail.next
                self.cache[key].prev = self.tail
                self.tail = self.cache[key]
        else:
            if not self.cache:
                self.lead = Things(key, value)
                self.tail = self.lead
                self.cache[key] = self.lead
            else:
                self.tail.next = Things(key, value)
                self.cache[key] = self.tail.next
                self.cache[key].prev = self.tail
                self.tail = self.cache[key]

class Things:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)