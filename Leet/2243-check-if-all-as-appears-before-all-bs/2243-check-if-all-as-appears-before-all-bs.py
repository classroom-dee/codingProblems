class Solution:
    def checkString(self, s: str) -> bool:
        string = 'a'
        switch_count = 0
        for c in s:
            if c != string:
                string = 'b'
                switch_count += 1
        return switch_count < 2
