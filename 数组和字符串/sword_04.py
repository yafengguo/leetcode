from math import ceil
from typing import List
import numpy as np


class Solution:

    @staticmethod
    def findNumberIn2DArray(matrix: List[List[int]], target: int) -> bool:
        # print("findNumberIn2DArray matrix=", matrix, "target =", target)
        A = np.array(matrix)
        n = len(matrix)
        if n == 0:
            return False
        m = len(matrix[0])
        if m == 0:
            return False
        min_idx = min(n, m) - 1
        res = Solution.halfSearch(matrix, target, 0, 2, 0, min_idx)
        if n == m or res:
            return res
        if n > m:
            newMatrix = A[min_idx + 1:, :].tolist()
        else:
            newMatrix = A[:, min_idx + 1:].tolist()
        return Solution.findNumberIn2DArray(newMatrix, target)

        # first search from diag (half search) then search in x and y direction respectively (two round half search)
        # if last row then do a y direction search.

    @staticmethod
    def halfSearch(matrix: List[List[int]], target: int, offset: int = 0, direction: int = 0, start: int = 0,
                   end: int = 0) -> bool:
        """
        half search
        :param offset:
        :param matrix:
        :param target: target to search for
        :param direction: 0: x axis direction; 1: y axis direction. 2: diag direction.
        :param start: start offset
        :param end: end offset.
        :return:
        """
        # print("half search; offset=", offset, " direction=", direction, " start=", start, " end=", end, " ")
        if start > end:
            return False
        if abs(end - start) < 2:
            if direction == 2:
                offset = end
            temp1 = Solution.getItem(matrix, offset, direction, start)
            temp2 = Solution.getItem(matrix, offset, direction, end)
            if temp1 == target or temp2 == target:
                return True
            elif direction != 2:
                return False
            colExist = Solution.halfSearch(matrix, target, offset, 0, 0, offset)
            if colExist:
                return True
            rowExist = Solution.halfSearch(matrix, target, offset, 1, 0, offset)
            if rowExist:
                return True
            res2 = False
            if end < max(len(matrix), len(matrix[0])) - 1:
                # need search again after exclude this this section.
                A = np.array(matrix)
                newMatrix1 = A[0:offset:, offset + 1:].tolist()
                res1 = Solution.findNumberIn2DArray(newMatrix1, target)
                if not res1:
                    newMatrix2 = A[offset + 1:, 0:offset].tolist()
                    res2 = Solution.findNumberIn2DArray(newMatrix2, target)
                else:
                    return True
            return res2
        else:
            idx = start + ceil((end - start) / 2)
            if direction == 2:
                offset = idx
            half = Solution.getItem(matrix, offset, direction, idx)
            # print("value got:", half)
            if half == target:
                return True
            elif half < target:
                return Solution.halfSearch(matrix, target, offset, direction, idx, end)
            else:
                return Solution.halfSearch(matrix, target, offset, direction, start, idx)

    @staticmethod
    def getItem(matrix: List[List[int]], offset: int = 0, direction: int = 0, idx: int = 0):
        # print("checking offset:", offset)
        # print("checking idx:", idx)
        if direction == 2:
            return matrix[idx][idx]
        elif direction == 0:
            return matrix[offset][idx]
        elif direction == 1:
            return matrix[idx][offset]


if __name__ == '__main__':
    s = Solution()
    # l = [
    #     [1,   4,  7, 11, 15],
    #     [2,   5,  8, 12, 19],
    #     [3,   6,  9, 16, 22],
    #     [10, 13, 14, 17, 24],
    #     [18, 21, 23, 26, 30]
    # ]
    #
    #

    l = [
        [1, 3, 5, 7, 9],
        [2, 4, 6, 8, 10],
        [11, 13, 15, 17, 19],
        [12, 14, 16, 18, 20],
        [21, 22, 23, 24, 25]]
    t = s.findNumberIn2DArray(l, 11)
    print(t)
