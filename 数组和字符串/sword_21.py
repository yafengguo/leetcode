# 题目描述
# 输入一个整数数组，实现一个函数来调整该数组中数字的顺序，使得所有的奇数位于数组的前半部分，
# 所有的偶数位于数组的后半部分，并保证奇数和奇数，偶数和偶数之间的相对位置不变。

class Solution:
    def reOrderArray(self, array):
        # write code here
        k = len(array)
        if k == 0:
            return array
        i = 0
        j = 1

        while i < k and j < k:
            while i < k and array[i] % 2 == 1:
                i = i + 1
            j = i + 1

            while j < k and array[j] % 2 == 0:
                    j = j + 1
            tmp_odd = array[i]
            if i < k and j < k:
                array[i] = array[j]
            p = j - 1

            while p > i and array[p] % 2 == 0 and j < k:
                array[p], array[j] = array[j], array[p]
                j = p
                p = p - 1
            if p+1 < k:
                array[p+1] = tmp_odd

        return array


if __name__ == "__main__":
    s = Solution()
    print(s.reOrderArray([]))
