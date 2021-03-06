# 给定一个字符串，请你找出其中不含有重复字符的 最长子串 的长度。
#
# 示例 1:
#
# 输入: "abcabcbb"
# 输出: 3
# 解释: 因为无重复字符的最长子串是 "abc"，所以其长度为 3。
# 示例 2:
#
# 输入: "bbbbb"
# 输出: 1
# 解释: 因为无重复字符的最长子串是 "b"，所以其长度为 1。
# 示例 3:
#
# 输入: "pwwkew"
# 输出: 3
# 解释: 因为无重复字符的最长子串是 "wke"，所以其长度为 3。
#      请注意，你的答案必须是 子串 的长度，"pwke" 是一个子序列，不是子串。
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/longest-substring-without-repeating-characters
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
# 其他滑动窗口的题目
# 3. 无重复字符的最长子串
# 30. 串联所有单词的子串
# 76. 最小覆盖子串
# 159. 至多包含两个不同字符的最长子串
# 209. 长度最小的子数组
# 239. 滑动窗口最大值
# 567. 字符串的排列
# 632. 最小区间
# 727. 最小窗口子序列

# 作者：powcai
# 链接：https://leetcode-cn.com/problems/longest-substring-without-repeating-characters/solution/hua-dong-chuang-kou-by-powcai/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        """
         思路： 构建滑动窗口。当右侧字符不重复时，扩展窗口将其纳入窗口内。
         当右侧字符在窗口内有重复字符时，收缩窗口左侧排除掉重复字符，再讲右侧字符纳入窗口内。
         重复上述操作，直到窗口到达字符串末端。在此过程中，记录窗口的最大长度。
        :param s: 输入字符串
        :return:  无重复字符最长子串长度
        """
        if not s:
            return 0
        i = 0
        j = 1
        max_len = 1
        while i < len(s) and j <= len(s):
            if s[j:j + 1] not in s[i:j]:
                j = j + 1
                if j - i > max_len:
                    max_len = j - i
            else:
                i = i + s[i:j].index(s[j:j + 1]) + 1
        return max_len


if __name__ == '__main__':
    s = Solution()
    t = s.lengthOfLongestSubstring(" ")
    print(t)
