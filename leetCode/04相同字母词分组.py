"""给你一个字符串数组，请你将 字母异位词 组合在一起。可以按任意顺序返回结果列表。
字母异位词 是由重新排列源单词的所有字母得到的一个新单词。
示例 1:
输入: strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
输出: [["bat"],["nat","tan"],["ate","eat","tea"]]

示例 2:
输入: strs = [""]
输出: [[""]]

示例 3:
输入: strs = ["a"]
输出: [["a"]]
"""
from collections import defaultdict

class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        # 创建一个默认字典，值为列表
        anagrams = defaultdict(list)
        print("打印默认字典结果：", anagrams)
        # 遍历字符串数组
        for s in strs:
            # 将字符串排序后作为键
            print("遍历后取值为：", s)
            sorted_str = ''.join(sorted(s))
            print("sorted_str的值为：", sorted_str)
            # 将原字符串添加到对应键的列表中
            anagrams[sorted_str].append(s)
            print("for循环里面的anagrams为：", anagrams)
        print("anagrams.values():", anagrams.values())
        return list(anagrams.values())


strs1 = ["eat", "tea", "tan", "ate", "nat", "bat"]
s2 = Solution()
s2.groupAnagrams(strs1)