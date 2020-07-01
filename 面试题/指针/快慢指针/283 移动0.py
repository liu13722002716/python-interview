"""
:Author: Mr.Liu
:Create: 2020/6/22 15:25
:Github: https://XXXXXXXX
Copyright (c) 2020,Mr.Liu Group All Rights Reserved.
"""
"""
leetcode 283 - 移动零
问题描述
给定一个数组 nums，编写一个函数将所有 0 移动到数组的末尾，同时保持非零元素的相对顺序。

示例:
    输入: [0,1,0,3,12]
    输出: [1,3,12,0,0]
说明:
必须在原数组上操作，不能拷贝额外的数组。
尽量减少操作次数。
"""


# 方法1
from typing import List
class Solution:
    def removeZeroes(self, nums: List[int]) -> None:
        slow = 0 # 慢指针
        fast = 0 # 快指针
        while fast < len(nums):
            if nums[fast] == 0:
                fast += 1
            else:
                nums[slow],nums[fast] = nums[fast],nums[slow] # 将等于0的位置与后面不等于0的数值交换位置
                slow += 1
                fast += 1
        return nums

if __name__ == '__main__':
    s = Solution()
    print(s.removeZeroes([0,1,0,3,12]))

# 方法2
class Solution:
    def removeZeroes(self,nums:List):
        slow = 0 # 慢指针
        fast = 0 # 快指针
        while fast < len(nums):
            if nums[fast] == 0:
                fast += 1
            else:
                nums[slow] = nums[fast] # 将后面不等于0的数值赋值给等于0的位置
                slow += 1
                fast += 1
        for i in range(slow,len(nums)): # fast 指针遍历完后slow之后的数值都应变成0,所以在加一个循环判断
            nums[i] = 0
        return nums
if __name__ == '__main__':
    s = Solution()
    print(s.removeZeroes([0,1,0,3,12]))