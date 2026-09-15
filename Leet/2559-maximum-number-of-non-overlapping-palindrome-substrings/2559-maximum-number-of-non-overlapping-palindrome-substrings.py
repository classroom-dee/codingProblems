class Solution:
    def maxPalindromes(self, s, k):
        n = len(s)
        # =========================================================
        # Palindrome check

        # pal[start][end] == True
        # means: s[start...end] is a palindrome.
        pal = [[False] * n for _ in range(n)]

        # Every single character is automatically a palindrome.
        # So:
        # pal[0][0] = True
        # pal[1][1] = True
        # pal[2][2] = True
        # ...
        for i in range(n):
            pal[i][i] = True

        # for longer substrings,
        # Suppose we're checking:
        #
        #       j              i
        #       â              â
        #       a  b  c  c  b  a
        #
        # For the WHOLE thing to be a palindrome:
        #
        # 1. The outside characters must match
        # 2. The inside must already be a palindrome. So, 
        # pal[j][i] =
        #     s[j] == s[i]
        #     AND
        #     pal[j+1][i-1]
        #
        # This is why we process shorter substrings before
        # longer substrings.
        for length in range(2, n + 1):
            for j in range(0, n - length + 1):
                # If the substring starts at j and has this length,
                # its ending index is:
                i = j + length - 1

                # First check the outside characters.
                if s[j] != s[i]:
                    pal[j][i] = False
                    continue

                # If the length is exactly 2 like: "aa",
                # then matching outside characters are enough.
                # There is no "inside substring" to check.
                if length == 2:
                    pal[j][i] = True
                    continue

                # Otherwise:
                #
                #      j           i
                #      â           â
                #      a  b  c  b  a
                #         â     â
                #        j+1   i-1
                #
                # We already know whether the inside is a palindrome.
                if pal[j + 1][i - 1]:
                    pal[j][i] = True

        # =========================================================
        # Do the DP
        #
        # dp[i] means:
        # maximum number of non-overlapping palindromes,
        # each with length >= k,
        # that can be selected from s[0...i]
        dp = [0] * n

        for i in range(n):
            # Case 1: Don't select a palindrome ending at i.
            # If index i doesn't help us create another palindrome,
            # we can simply keep the answer we already had for
            # s[0...i-1].
            if i == 0:
                # There is no dp[-1] conceptually.
                # Before the string starts, we have selected
                # zero palindromes.
                dp[i] = 0
            else:
                dp[i] = dp[i - 1]

            # Case 2: Try to select a palindrome at j...i
            for j in range(i + 1):
                # First calculate the length of s[j...i]
                length = i - j + 1

                # It isn't allowed if it's shorter than k.
                if length < k:
                    continue

                # Palindrome check with the precalculated matrix.
                if pal[j][i] == False:
                    continue

                # At this point, s[j...i] fits the bill
                # So select it:
                # [ 0 ........ j-1 ][ j ........ i ]
                #      old stuff     new palindrome
                # Since the substrings cannot overlap, any
                # palindromes we selected BEFORE this one must
                # finish before j.
                # That means they must live inside: s[0...j-1]
                # What was the best answer BEFORE j?
                if j == 0:
                    previous_best = 0
                else:
                    previous_best = dp[j - 1]

                # We take everything we could select before j
                # +
                # this new palindrome.
                candidate = previous_best + 1

                # dp[i] might already contain a good answer.
                # So we keep **whichever gives us more palindromes.**
                # Compare against the best answer we've found
                # for dp[i]. Best hoarder wins.
                dp[i] = max(dp[i], candidate)

        return dp[n - 1]