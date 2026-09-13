class Solution:
    def largestOverlap(self, img1: List[List[int]], img2: List[List[int]]) -> int:
        # from collections import deque
        # if len(img1) == 1:
        #     if img1[0][0] == img2[0][0] == 1:
        #         return 1
        #     else:
        #         return 0

        # # translations for left, right, up, down
        # tf = [(0, -1), (0, 1), (-1, 0), (1, 0)]
        # def _translate(img, direction: int):
        #     new = [[0] * len(img[0]) for _ in range(len(img))]
        #     for i in range(len(img)):
        #         for j in range(len(img[i])):
        #             dest_row, dest_col = i + tf[direction][0], j + tf[direction][1]
        #             if 0 <= dest_row < len(img) and 0 <= dest_col < len(img[i]):
        #                 new[dest_row][dest_col] = img[i][j]
        #     match direction:
        #         case 0:
        #             for row in new:
        #                 row[-1] = 0
        #         case 1:
        #             for row in new:
        #                 row[0] = 0
        #         case 2:
        #             new[-1] = [0] * len(img[0])
        #         case 3:
        #             new[0] = [0] * len(img[0])
        #         case _:
        #             print("Burp")
        #     return new
        
        # def _flatten(img):
        #     return ''.join(map(str, [cell for row in img for cell in row]))

        # def _overlap_sum(flat_img1, flat_img2):
        #     b = bin(int(flat_img1, 2) & int(flat_img2, 2))[2:]
        #     return sum((int(x) for x in b))

        # img2_flattened = _flatten(img2)
        # q = deque((img1,))
        # visited = set()
        # mx = 0

        # while q:
        #     curr_img = q.popleft()
        #     tup = tuple(tuple(row) for row in curr_img)
        #     if tup in visited:
        #         continue
        #     visited.add(tup)
        #     for d in [0, 1, 2, 3]:
        #         curr_moved = _translate(curr_img, d)
        #         curr_moved_flattened = _flatten(curr_moved)
        #         s = _overlap_sum(curr_moved_flattened, img2_flattened)
        #         mx = max(mx, s)
        #         q.append(curr_moved)
        #     if mx == len(img1) * len(img1[0]):
        #         break

        # return mx

        # ððððð nope
        n = len(img1)

        ones1 = []
        ones2 = []

        for i in range(n):
            for j in range(n):
                if img1[i][j]:
                    ones1.append((i, j))
                if img2[i][j]:
                    ones2.append((i, j))

        shifts = Counter()

        for x1, y1 in ones1:
            for x2, y2 in ones2:
                # freqs of offsets betweem tje twp images
                shifts[(x2-x1, y2-y1)] += 1
        # the most frequent shift becomes the max overlap sum
        return max(shifts.values(), default=0)