"""
:Author: Mr.Liu
:Create: 2020/6/27 9:58
:Github: https://XXXXXXXX
Copyright (c) 2020,Mr.Liu Group All Rights Reserved.
"""
"""
给你一个未排序的整数数组，请你找出其中没有出现的最小的正整数。
示例 1:
    输入: [1,2,0]
    输出: 3
示例 2:
    输入: [3,4,-1,1]
    输出: 2
示例 3:
    输入: [7,8,9,11,12]
    输出: 1
提示：
    你的算法的时间复杂度应为O(n)，并且只能使用常数级别的额外空间。
"""

from typing import List
class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        i = 1
        while i in nums:
            i += 1
        return i
if __name__ == '__main__':
    s = Solution()
    print(s.firstMissingPositive([3,4,-1,1]))
