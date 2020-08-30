# 题目描述
# 输入一个矩阵，按照从外向里以顺时针的顺序依次打印出每一个数字，例如，如果输入如下4 X 4矩阵：
# 1 2 3 4
# 5 6 7 8
# 9 10 11 12
# 13 14 15 16
# 则依次打印出数字1,2,3,4,8,12,16,15,14,13,9,5,6,7,11,10.
from typing import List


class Solution:
    def printMatrix(self, matrix: List[List[int]]):
        n = len(matrix)
        if n == 0:
            return []
        m = len(matrix[0])
        if m == 0:
            return []
        res = []
        top_left = [0, 0]
        top_right = [0, m - 1]
        bottom_left = [n - 1, 0]
        bottom_right = [n - 1, m - 1]
        while top_left[1] <= top_right[1] and top_left[0] <= bottom_left[0]:
            res = res + self.getTopRow(matrix, top_left, top_right, bottom_left, bottom_right)
            top_left[0] = top_left[0] + 1
            top_right[0] = top_right[0] + 1
            res = res + self.getRightRow(matrix, top_left, top_right, bottom_left, bottom_right)
            top_right[1] = top_right[1] - 1
            bottom_right[1] = bottom_right[1] - 1
            a = self.getBottomRow(matrix, top_left, top_right, bottom_left, bottom_right)
            a.reverse()
            res = res + a
            bottom_left[0] = bottom_left[0] - 1
            bottom_right[0] = bottom_right[0] - 1
            a = self.getLeftRow(matrix, top_left, top_right, bottom_left, bottom_right)
            a.reverse()
            res = res + a
            top_left[1] = top_left[1] + 1
            bottom_left[1] = bottom_left[1] + 1
        return res

    def getTopRow(self, A, top_left, top_right, bottom_left, bottom_right):
        if top_left[1] >= 0 and top_left[0] >= 0 and top_right[1] >= 0 and \
                bottom_left[0] >= 0 and bottom_right[1] >= 0 and bottom_left[1] >= 0:
            return [sublist[top_left[1]:top_right[1] + 1] for sublist in A][top_left[0]]
        else:
            return []

    def getBottomRow(self, A, top_left, top_right, bottom_left, bottom_right):
        if bottom_left[0] >= top_left[0] >= 0 and bottom_right[1] >= 0 and bottom_left[1] >= 0 and \
                top_left[1] >= 0 and top_left[0] >= 0 and top_right[1] >= 0:
            return [sublist[bottom_left[1]:bottom_right[1] + 1] for sublist in A][bottom_left[0]]
        else:
            return []

    def getLeftRow(self, A, top_left, top_right, bottom_left, bottom_right):
        if top_left[0] >= 0 and top_right[1] >= top_left[1] >= 0 and bottom_left[0] >= 0 and \
                bottom_right[0] >= 0 and top_right[1] >= 0 and top_right[0] >= 0:
            return [sublist[top_left[1]] for sublist in A][top_left[0]:bottom_left[0] + 1]
        else:
            return []

    def getRightRow(self, A, top_left, top_right, bottom_left, bottom_right):
        if bottom_right[0] >= 0 and top_right[1] >= 0 and top_right[0] >= 0 and \
                top_left[0] >= 0 and top_left[1] >= 0 and bottom_left[0] >= 0:
            return [sublist[top_right[1]] for sublist in A][top_right[0]:bottom_right[0] + 1]
        else:
            return []


if __name__ == '__main__':
    s = Solution()
    l = [[1,2,3,4,5]]

    t = s.printMatrix(l)
    print(t)
