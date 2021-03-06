# 牛客最近来了一个新员工Fish，每天早晨总是会拿着一本英文杂志，写些句子在本子上。
# 同事Cat对Fish写的内容颇感兴趣，有一天他向Fish借来翻看，但却读不懂它的意思。
# 例如，“student. a am I”。后来才意识到，这家伙原来把句子单词的顺序翻转了，
# 正确的句子应该是“I am a student.”。Cat对一一的翻转这些单词顺序可不在行，你能帮助他么？

# -*- coding:utf-8 -*-
class Solution:
    def ReverseSentence(self, s):
        # write code here
        temp = s.split(" ")
        res = []
        for i in range(len(temp)):
            res.append(temp[len(temp) - i -1])
        return " ".join(res)



if __name__ == '__main__':
    s = Solution()
    l = "student. a am I"
    t = s.ReverseSentence(l)
    print(t)

# [1,2,4,7,11,15],15
# [1,2,4,7,11,16],10
