# the optimization follow-up
def _rev_bits(n):
    _reversed = 0
    for _ in range(8):
        last_bit = n & 1
        _reversed = (_reversed << 1) | last_bit
        n = n >> 1
    return _reversed

bits_lookup = [_rev_bits(n) for n in range(256)]

class Solution:

    def reverseBits(self, n: int) -> int:
        _reversed = 0
        for _ in range(4):
            last_8_bit = n & 255
            last_8_bit_reversed = bits_lookup[last_8_bit]
            _reversed = (_reversed << 8) | last_8_bit_reversed
            n = n >> 8
        # orig = n
        # reversed = 0
        # for _ in range(32):
        #     last_bit = n & 1
        #     reversed = (reversed << 1) | last_bit
        #     n = n >> 1

        # print(f"original: {orig:032b}")
        # print(f"reversed: {reversed:032b}")

        return _reversed