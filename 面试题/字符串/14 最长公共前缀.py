"""
:Author: Mr.Liu
:Create: 2020/6/29 20:50
:Github: https://XXXXXXXX
Copyright (c) 2020,Mr.Liu Group All Rights Reserved.
"""
"""
14 编写一个函数来查找字符串数组中的最长公共前缀。
链接：https://leetcode-cn.com/problems/longest-common-prefix
示例 1:
    输入: ["flower","flow","flight"]
    输出: "fl"
示例 2:
    输入: ["dog","racecar","car"]
    输出: ""
    解释: 输入不存在公共前缀。
"""

# a = [1, 2, 3]
# b = [4, 5, 6]
# zipped = list(zip(a, b))
# print(zipped)
# for each in zipped:
#     print(each)
#
# zipped = ["flower", "flow", "flight"]
# for each in zip(*zipped):
#     print(each)
#
# strs = ["flower", "flow", "flight"]
# minLength = min([len(s) for s in strs])
# print(minLength)

from typing import List
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        res = ""
        if len(strs) == 0 or "" in strs:  # 当 strs 列表为空时,或者列表中有一个或多个字符串为空,那么他们就没有公共前缀,所以返回空
            return ""
        if len(strs) == 1:  # 当列表中只有一个字符串时,那么它本身就是自己的公共前缀,所以返回列表的第一个字符串即可
            return strs[0]
        minLength = min([len(s) for s in strs])   # 从列表中选取一个最小长度的字符串,再开始定义它为最小长度,如果其中的字符全部以这个最小字符串开头,那么他们最大的公共前缀也就是这个字符串的长度
        publicWord = []  # 接收变量
        for i in range(minLength):
            for word in strs:   # 遍历列表
                publicWord.append(word[:i+1])  # 用变量接受每一个字符串的开始到 i+1 位,刚开始也就是保存没有一个字符串的第一位字母
            if len(set(publicWord)) == 1:  # 当字符串里面不重复的字符等于 1 时,证明第一位字符是他们的公共前缀
                publicWord = []  # 再次定义变量为空,继续判断,接受变量
            else:
                return strs[0][:i]  # 最后输出,列表中第一位的,前 i 位字符,不包括 i ,就是他们的最长的公共前缀
        return strs[0][:i+1]

if __name__ == '__main__':
    s = Solution()
    print(s.longestCommonPrefix(["c","c"]))

# ["flower", "flow", "flight"]
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        res = ''  # 定义一个空字符串作为,接收公共前缀的变量
        for each in zip(*strs):  # 遍历压缩 strs 列表,每次输出的是每个字符的第一位开始,每次按顺序输出每一个字符串的其中一个字符
            if len(set(each)) == 1:  # 当字符串里面不重复的字符等于 1 时,证明第一位字符是他们的公共前缀
                res += each[0]  # 接收变量保存,如果下一位也是,那么接收变量将继续增加下一个字符
            else:  # 如果当字符串里面不重复的字符不等于 1 时,证明该个字符不完全一样,证明此时就不是公共前缀  ,所以返回之前保存公共前缀的变量
                return res
        return res

if __name__ == '__main__':
    s = Solution()
    print(s.longestCommonPrefix(["c","c"]))

