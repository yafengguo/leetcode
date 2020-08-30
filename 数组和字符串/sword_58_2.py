# 汇编语言中有一种移位指令叫做循环左移（ROL），现在有个简单的任务，
# 就是用字符串模拟这个指令的运算结果。对于一个给定的字符序列S，请你
# 把其循环左移K位后的序列输出。例如，字符序列S=”abcXYZdef”,要求
# 输出循环左移3位后的结果，即“XYZdefabc”。是不是很简单？OK，搞定它！

# -*- coding:utf-8 -*-
class Solution:
    def LeftRotateString(self, s, n):
        if n <= 0:
            return s
        if len(s) == 0:
            return s
        if n > len(s):
            n = n % len(s)
        s1 = s[n:]
        s2 = s[0:n]
        return s1 + s2


if __name__ == '__main__':
    s = Solution()
    l = ""
    t = s.LeftRotateString(l, 6)
    print(t)

# [1,2,4,7,11,15],15
# [1,2,4,7,11,16],10
