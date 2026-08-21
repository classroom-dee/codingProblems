# optimization follow up
table = [0] * 0x10000 # the num of 16 bit values
def _init_table():
    for i in range(1, 0x10000, 1):
        table[i] = table[i >> 1] + (1 & i)

_init_table()

class Solution:
    def hammingWeight(self, n: int) -> int:
        # naive
        # m1 = int("01"*32, base=2)
        # m2 = int("0011"*16, base=2)
        # m4 = int("00001111"*8, base=2)
        # m8 = int("0000000011111111"*4, base=2)
        # m16 = int("00000000000000001111111111111111"*2, base=2)
        # m32 = int("0"*32 + "1"*32, base=2)
        # n = (n & m1) + ((n >> 1) & m1)
        # n = (n & m2) + ((n >> 2) & m2)
        # n = (n & m4) + ((n >> 4) & m4)
        # n = (n & m8) + ((n >> 8) & m8)
        # n = (n & m16) + ((n >> 16) & m16)
        # n = (n & m32) + ((n >> 32) & m32)
        # return n
        # the largest 16 bit value = 0xFFFF
        return table[n & 0xFFFF] + table[n >> 16]