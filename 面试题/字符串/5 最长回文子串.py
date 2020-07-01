"""
:Author: Mr.Liu
:Create: 2020/6/29 11:58
:Github: https://XXXXXXXX
Copyright (c) 2020,Mr.Liu Group All Rights Reserved.
"""
"""
给定一个字符串 s，找到 s 中最长的回文子串。你可以假设 s 的最大长度为 1000。
示例 1：
    输入: "babad"
    输出: "bab"
    注意: "aba" 也是一个有效答案。
示例 2：
    输入: "cbbd"
    输出: "bb"
"""

class Solution:
    def longestPalindrome(self, s: str) -> str:
        lenth = len(s)
        if lenth < 2:
            return s
        maxlen = 1  # 先定义最大长度为1
        res = s[0] # 返回最长会问子串的接收变量
        for i in range(lenth - 1):
            odd = self.centerSpread(s,i,i)
            even = self.centerSpread(s,i,i+1)
            maxstr = odd if len(odd) > len(even) else even
            if len(maxstr) > maxlen:
                maxlen = len(maxstr)
                res = maxstr
        return res

    def centerSpread(self,s: str ,left: int,right: int):
        lenth = len(s)
        i = left   # 利用分散双指针,滑动窗口
        j = right
        while i >= 0 and j < lenth:
            if s[i] == s[j]:
                i -= 1
                j += 1
            else:
                break
        return s[i+1:j]

if __name__ == '__main__':
    s = Solution()
    print(s.longestPalindrome("babad"))