from collections import deque

class StreamChecker:
    def __init__(self, words: list[str]):
        self.words = {}
        self.max_length = 0
        for word in words:
            self.init_trie(word, len(word) - 1, self.words)
            self.max_length = max(self.max_length, len(word))
        self.suffix = deque(maxlen=self.max_length)

    def init_trie(self, word, idx, node: dict):
        if idx < 0:
            node["."] = {}
            return
        self.init_trie(word, idx - 1, node.setdefault(word[idx], {}))
        # if word[idx] in node:
        #     self.init_trie(word, idx - 1, node[word[idx]])
        # else:
        #     node[word[idx]] = {}
        #     self.init_trie(word, idx - 1, node[word[idx]])
        
    def __repr__(self):
        return f"{self.words}"

    def query(self, letter: str) -> bool:
        # if len(self.suffix) >= self.max_length:
        #     self.suffix = ''.join(self.suffix[i] for i in range(1, len(self.suffix))) + letter
        # else:
        #     self.suffix += letter
        self.suffix.append(letter)
        if self.words.get(letter) is not None:
            return self.search()
        else:
            return False

    def search(self):
        node = self.words
        # i = len(self.suffix) - 1
        # while i > -1:
            # i -= 1
        for char in reversed(self.suffix):
            if char in node:
                if "." in node[char]:
                    return True
                else:
                    node = node[char]
            else:
                return False
        return False

# Your StreamChecker object will be instantiated and called as such:
# obj = StreamChecker(words)
# param_1 = obj.query(letter)