class Solution:
    def sumGame(self, num: str) -> bool:
        # init game
        first, second = num[:len(num) // 2], num[len(num) // 2:]
        f_sum, s_sum = 0, 0
        f_rem, s_rem = 0, 0
        for f, s in zip(first, second):
            if f.isdigit(): f_sum += int(f)
            else: f_rem += 1
            if s.isdigit(): s_sum += int(s)
            else: s_rem += 1
        
        # if the num of remaining turns is an odd number, alice wins because she starts first
        if (f_rem + s_rem) % 2:
            return True

        # even number of remaining turns:
        # bob can control "alice's choice + bob's choice = 9" (constraint 0 <= n <= 9)
        # so, if the first half is ahead, 
        # extra choices on the second half can compensate for that.
        # bob loses if the sum is out of reach: "diff is not equal to (controlled number) * (pairs of turns)"
        return f_sum - s_sum != 9 * (s_rem - f_rem) / 2
        
        # while f_rem or s_rem:
        #     if f_sum >= s_sum and f_rem:
        #         f_rem -= 1
        #     elif f_sum <= s_sum and s_rem:
        #         s_rem -= 1
        #     elif f_sum <= s_sum and f_rem:
        #         f_sum += min(s_sum - f_sum, 9)
        #         f_rem -= 1
        #     elif f_sum >= s_sum and s_rem:
        #         s_sum += min(f_sum - s_sum, 9)
        #         s_rem -= 1
            
        # return f_sum != s_sum