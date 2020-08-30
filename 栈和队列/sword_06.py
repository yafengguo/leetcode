# 输入一个链表，按链表从尾到头的顺序返回一个ArrayList。

# -*- coding:utf-8 -*-
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # 返回从尾部到头部的列表值序列，例如[1,2,3]
    def printListFromTailToHead(self, listNode):
        res = []
        if listNode:
            while listNode.next:
                res.append(listNode.val)
                listNode = listNode.next
            res.append(listNode.val)
        res.reverse()
        return res


if __name__ == '__main__':
    a = ListNode(1)
    b = ListNode(2)
    c = ListNode(3)
    a.next = b
    b.next = c
    s = Solution()
    # l = [
    #     [-5]]
    t = s.printListFromTailToHead(a)
    print(t)
