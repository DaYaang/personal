"""
给定一个字符串 s ，请你找出其中不含有重复字符的 最长子串的长度。
示例 1:
输入: s = "abcabcbb"
输出: 3
解释: 因为无重复字符的最长子串是 "abc"，所以其长度为 3。
示例 2:
输入: s = "bbbbb"
输出: 1
解释: 因为无重复字符的最长子串是 "b"，所以其长度为 1。

示例 3:
输入: s = "pwwkew"
输出: 3
解释: 因为无重复字符的最长子串是 "wke"，所以其长度为 3。
     请注意，你的答案必须是 子串 的长度，"pwke" 是一个子序列，不是子串。
"""

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        # 处理字符去重
        single_str_set = set()
        str_list  = list(s)
        for ss in str_list:
            single_str_set.add(ss)
        print(single_str_set,len(single_str_set))

        str_list = []
        for i in range(0,len(s)-1):
            for j in range(i+1,len(s)):
                if len(s[i:j])==len(single_str_set):
                    str_list.append(s[i:j])
        print(str_list)
        for str in str_list:
            print(len(str),len(set(str)))
            if len(str) != len(set(str)):

                str_list.remove(str)

        print(str_list[0])

s = "pwwkew"
s1 = Solution()
s1.lengthOfLongestSubstring(s)
#
# sl1 = {'bc', 'abc', 'cab', 'abcb', 'a', 'abca', 'abcab', 'bcab', 'c', 'abcabc', 'bcb', 'bcabcb', 'b', 'bcabc', 'cb', 'ca', 'ab', 'bca', 'cabc', 'abcabcb', 'cabcb'}
# print((sl1))
