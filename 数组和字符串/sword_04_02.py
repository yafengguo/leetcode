

class Solution:

    @staticmethod
    def findNumberIn2DArray(matrix: List[List[int]], target: int) -> bool:
        # print("findNumberIn2DArray matrix=", matrix, "target =", target)
        n = len(matrix)
        if n == 0:
            return False
        m = len(matrix[0])
        if m == 0:
            return False

        res = False
        i = n - 1
        j = 0
        while not res and i >= 0 and j <= m - 1:
            if matrix[i][j] == target:
                return True
            elif matrix[i][j] > target:
                i = i - 1
            else:
                j = j + 1
        return res

        # first search from diag (half search) then search in x and y direction respectively (two round half search)
        # if last row then do a y direction search.


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
        [-5]]
    t = s.findNumberIn2DArray(l, -5)
    print(t)
