class Solution:
    def maximumWeight(self, intervals: List[List[int]]) -> List[int]:
        from bisect import bisect_left
        from typing import List
        # Attach each interval's original index.
        #
        # Each item becomes:
        # [left, right, weight, original_index]
        items = []

        for index, (left, right, weight) in enumerate(intervals):
            items.append([left, right, weight, index])

        # Sort by right endpoint.
        # This lets us use weighted-interval-scheduling style DP.
        items.sort(key=lambda interval: interval[1])

        n = len(items)

        # Store all right endpoints separately so we can binary-search them.
        right_ends = [interval[1] for interval in items]

        # prev[i] = index of the last interval that ends STRICTLY before
        # interval i starts.
        #
        # If there is no such interval, prev[i] = -1.
        prev = [-1] * n

        for i in range(n):
            left = items[i][0]

            # We want:
            # right_end < left
            #
            # bisect_left(right_ends, left) gives the first position where
            # right_end >= left.
            #
            # So one position before that is the final interval satisfying:
            # right_end < left
            position = bisect_left(right_ends, left, 0, i)

            prev[i] = position - 1

        # dp[k][i] means:
        # best answer using the first i intervals
        # while choosing at most k intervals.
        #
        # Each state stores:
        # (total_weight, chosen_original_indices)
        #
        # We use n + 1 columns because column 0 means
        # "considering zero intervals".
        dp = [
            [(0, []) for _ in range(n + 1)]
            for _ in range(5)
        ]

        def better(option1, option2):
            """
            Return the better of two candidates.

            A candidate looks like:
                (score, indices)

            Rules:
            1. Higher score wins.
            2. If scores tie, lexicographically smaller index list wins.
            """

            score1, indices1 = option1
            score2, indices2 = option2

            if score1 > score2:
                return option1

            if score2 > score1:
                return option2

            # Same score -> lexicographically smaller list wins.
            if indices1 < indices2:
                return option1

            return option2

        # k = maximum number of intervals we're allowed to choose.
        for k in range(1, 5):

            # i represents how many sorted intervals we're considering.
            #
            # items[i - 1] is therefore the "current" interval.
            for i in range(1, n + 1):
                current = items[i - 1]

                left = current[0]
                right = current[1]
                weight = current[2]
                original_index = current[3]

                # ------------------------------------
                # OPTION 1:
                # Do NOT take the current interval.
                # ------------------------------------
                skip_current = dp[k][i - 1]

                # ------------------------------------
                # OPTION 2:
                # Take the current interval.
                # ------------------------------------

                previous_interval_index = prev[i - 1]

                # DP columns are shifted by 1.
                #
                # If previous_interval_index == -1,
                # this becomes column 0.
                previous_dp_column = previous_interval_index + 1

                previous_score, previous_indices = dp[k - 1][previous_dp_column]

                take_score = previous_score + weight

                # Add this interval's ORIGINAL index.
                #
                # Sort the index list because the problem compares returned
                # arrays lexicographically by their index values.
                take_indices = previous_indices + [original_index]
                take_indices.sort()

                take_current = (take_score, take_indices)

                # Pick whichever candidate is better.
                dp[k][i] = better(skip_current, take_current)

        # dp[4][n] =
        # best answer using all intervals while selecting at most 4.
        final_score, final_indices = dp[4][n]

        return final_indices