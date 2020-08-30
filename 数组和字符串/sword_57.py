# 输入一个递增排序的数组和一个数字S，在数组中查找两个数，使得他们的和正好是S，
# 如果有多对数字的和等于S，输出两个数的乘积最小的。

# -*- coding:utf-8 -*-
class Solution:
    def FindNumbersWithSum(self, array, tsum):
        # write code here
        if len(array) < 2:
            return []
        i = 0
        j = len(array) - 1
        res = []
        while i < j and len(res) == 0:
            temp = array[i] + array[j]
            if temp < tsum:
                i += 1
            if temp > tsum:
                j -= 1
            if temp == tsum:
                res.append((array[i], array[j]))
        if len(res) == 0:
            return []
        else:
            return res[0]


if __name__ == '__main__':
    s = Solution()
    l = []
    t = s.FindNumbersWithSum(l, 0)
    print(t)

# [1,2,4,7,11,15],15
# [1,2,4,7,11,16],10
