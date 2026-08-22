class Solution:
    def checkDivisibility(self, n: int) -> bool:
        def _digit_sum(n):
            if n < 10:
                return n
            return n % 10 + _digit_sum(n // 10)

        def _digit_prod(n):
            if n < 10:
                return n
            return (n % 10) * _digit_prod(n // 10)
        
        return n % (_digit_sum(n) + _digit_prod(n)) == 0
        
        