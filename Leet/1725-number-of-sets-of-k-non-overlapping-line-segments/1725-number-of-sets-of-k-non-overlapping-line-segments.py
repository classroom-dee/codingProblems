class Solution:
    def numberOfSets(self, n: int, k: int) -> int:
        """
        dp[i][segments][building]
        
        i: how many points we've processed
        
        segments: how many COMPLETE segments we've made
        
        building:
           0 = we are not currently building a segment
           1 = we currently have an open segment
        
        Each cell stores the NUMBER OF WAYS to reach that situation.
        """
        MOD = 10**9 + 7
        dp = []

        for i in range(n + 1):
            point_states = []

            for segments in range(k + 1):
                # [not_building, building]
                point_states.append([0, 0])

            dp.append(point_states)

        # Before processing any points:
        # - we've completed 0 segments
        # - we're not building anything
        # - there is exactly 1 way to be in this situation
        dp[0][0][0] = 1

        for i in range(n):

            for segments in range(k + 1):
                # --------------------------------
                # CASE 1: We're NOT building
                # --------------------------------
                ways = dp[i][segments][0]

                # Option 1:
                # Don't start a segment at this point.
                dp[i + 1][segments][0] += ways

                # Option 2:
                # Start a segment at this point.
                #
                # We haven't COMPLETED another segment yet,
                # so "segments" does not increase.
                dp[i + 1][segments][1] += ways

                # --------------------------------
                # CASE 2: We ARE building
                # --------------------------------
                ways = dp[i][segments][1]

                # Option 1:
                # Keep the segment open.
                dp[i + 1][segments][1] += ways

                # Option 2:
                # End the segment at this point.
                if segments < k:
                    dp[i + 1][segments + 1][0] += ways

                    # Important:
                    #
                    # Segments are allowed to share endpoints.
                    #
                    # So if we end one segment at this point,
                    # we can ALSO immediately start the next
                    # segment at this same point.
                    #
                    # Example:
                    #
                    # 0 ----- 2 ----- 4
                    #
                    # [0, 2] ends at 2
                    # [2, 4] starts at 2
                    #
                    dp[i + 1][segments + 1][1] += ways


                # Keep the numbers from becoming enormous.
                dp[i + 1][segments][0] %= MOD
                dp[i + 1][segments][1] %= MOD

                if segments < k:
                    dp[i + 1][segments + 1][0] %= MOD
                    dp[i + 1][segments + 1][1] %= MOD

        # We processed all n points.
        #
        # We want exactly k COMPLETE segments,
        # and we don't want an unfinished segment left open.
        return dp[n][k][0]
