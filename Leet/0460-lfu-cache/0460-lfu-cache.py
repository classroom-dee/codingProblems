class LFUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {} # {key: [Item, count]}
        # would be cleaner to have a class for count lookup ð¤·
        self.count_lookup = {} # {1: ItemList, 3: ItemList ...}
        self.total = 0
        self.min_freq = -1

    def evict(self):
        key = self.count_lookup[self.min_freq].head.key
        item_list = self.count_lookup[self.cache[key][1]]
        if item_list.length > 1:
            item_list.remove_item(self.cache[key][0])
        else:
            self.count_lookup.pop(self.cache[key][1])
        self.total -= 1
        self.cache.pop(key)

    def get(self, key: int) -> int:
        if not key in self.cache:
            return -1
        else:
            # old item
            count = self.cache[key][1]
            item_list = self.count_lookup[count]
            if item_list.length > 1:
                item_list.remove_item(self.cache[key][0])
            else:
                self.count_lookup.pop(self.cache[key][1])
            
            # new item
            self.cache[key][1] += 1
            count = self.cache[key][1]
            if self.count_lookup.get(count):
                item_list = self.count_lookup[count]
                item_list.add_item(self.cache[key][0])
            else:
                self.count_lookup[count] = ItemList(self.cache[key][0])
                item_list = self.count_lookup[count]

            old_count = count - 1
            if old_count == self.min_freq and old_count not in self.count_lookup:
                self.min_freq = count
            return self.cache[key][0].value

    def put(self, key: int, value: int) -> None:
        if key not in self.cache:
            new_item = Item(key, value)
            if self.total < self.capacity: # new
                if self.count_lookup.get(1):
                    item_list = self.count_lookup[1]
                    item_list.add_item(new_item)
                else:
                    self.count_lookup[1] = ItemList(new_item)
                self.total += 1
            else: # evict, then add
                self.evict()
                if self.count_lookup.get(1):
                    item_list = self.count_lookup[1]
                    item_list.add_item(new_item)
                else:
                    self.count_lookup[1] = ItemList(new_item)
                self.total += 1
            self.cache[key] = [new_item, 1]
            self.min_freq = 1
        else: # replace
            # old
            item, count_lookup_key = self.cache.pop(key)
            item_list = self.count_lookup[count_lookup_key]
            if item_list.length > 1:
                item_list.remove_item(item)
            else:
                self.count_lookup.pop(count_lookup_key)
            
            # new
            item.value = value
            self.cache[key] = [item, count_lookup_key + 1]
            count_lookup_key = self.cache[key][1]
            if self.count_lookup.get(count_lookup_key):
                item_list = self.count_lookup[count_lookup_key]
                item_list.add_item(item)
            else:
                self.count_lookup[count_lookup_key] = ItemList(item)
            
            old_count = count_lookup_key - 1
            if old_count == self.min_freq and old_count not in self.count_lookup:
                self.min_freq = count_lookup_key


class ItemList:
    def __init__(self, first):
        self.head = first
        self.tail = first
        # self.head.next = self.tail
        # self.tail.prev = self.head
        self.length = 1
    
    def replace_tail(self, item):
        self.tail.next = item
        item.prev = self.tail
        self.tail = item
        self.tail.next = None

    def move_item_to_tail(self, item):
        if item is self.tail or self.length == 1:
            pass
        elif item is self.head:
            self.head = item.next
            self.head.prev = None
            item.next = None
            self.replace_tail(item)    
        else:
            prv = item.prev
            nxt = item.next
            prv.next = nxt
            nxt.prev = prv
            self.replace_tail(item)
    
    def add_item(self, item):
        self.replace_tail(item)
        self.length += 1

    def remove_item(self, item):
        if item is self.tail:
            self.tail = item.prev
            self.tail.next = None
            item.prev = None
        elif item is self.head:
            self.head = item.next
            self.head.prev = None
            item.next = None
        else:
            prv = item.prev
            nxt = item.next
            prv.next = nxt
            nxt.prev = prv
            item.next, item.prev = None, None
        self.length -= 1
    

class Item:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None
        self.prev = None


# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)