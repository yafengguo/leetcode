# 数组中有一个数字出现的次数超过数组长度的一半，请找出这个数字。
# 例如输入一个长度为9的数组{1,2,3,2,2,2,5,4,2}。由于数字2在数组中出现了5次，超过数组长度的一半，因此输出2。如果不存在则输出0。

class Solution:

    def MoreThanHalfNum_Solution(self, numbers):
        if len(numbers) < 1:
            return 0
        map = {}
        for i in numbers:
            if i in map.keys():
                map[i] += 1
            else:
                map[i] = 1
            if map[i] > len(numbers) / 2:
                return i
        return 0


if __name__ == '__main__':
    s = Solution()
    arr = [1]

    t = s.MoreThanHalfNum_Solution(arr)
    print(t)
