class Solution:
    def lexGreaterPermutation(self, s: str, target: str) -> str:
        cnt = Counter(s)

        def _find(i, is_gt):
            """
            is_gt remembers whether it has beaten "target" or not.
            Once something greater is chosen, fill the remaining with the smallest.
            """
            if i == len(s):
                return "" if is_gt else None

            for c in sorted(cnt):
                if cnt[c] == 0:
                    continue

                if not is_gt and c < target[i]:
                    continue

                cnt[c] -= 1

                result = _find(i + 1, is_gt or c > target[i])

                cnt[c] += 1

                if result is not None:
                    return c + result

            return None

        res = _find(0, False)
        return "" if res is None else res