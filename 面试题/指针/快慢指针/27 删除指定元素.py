"""
:Author: Mr.Liu
:Create: 2020/6/22 16:57
:Github: https://XXXXXXXX
Copyright (c) 2020,Mr.Liu Group All Rights Reserved.
"""
"""
题目1
leetcode 27 移除元素
给定一个数组 nums 和一个值 val，你需要原地移除所有数值等于 val 的元素，返回移除后数组的新长度。
不要使用额外的数组空间，你必须在原地修改输入数组并在使用 O (1) 额外空间的条件下完成。
元素的顺序可以改变。你不需要考虑数组中超出新长度后面的元素。
示例 1:
给定 nums = [3,2,2,3], val = 3, 函数应该返回新的长度 2,
并且 nums 中的前两个元素均为 2。你不需要考虑数组中超出新长度后面的元素。

示例 2:
给定 nums = [0,1,2,2,3,0,4,2], val = 2, 函数应该返回新的长度 5,
并且 nums 中的前五个元素为 0, 1, 3, 0, 4。注意这五个元素可为任意顺序。
你不需要考虑数组中超出新长度后面的元素。
"""

# 方法1
from typing import List
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        slow = 0 # 慢指针
        fast = 0 # 快指针
        while fast < len(nums):
            # fast在slow的前面走
            # 如果 fast 值等于 val，则在slow位置不变fast位置向前移动一位
            if nums[fast] == val:
                fast += 1
            else:  # 如果 fast 值不等于 val，则在slow位置保存fast位置的数值,这样可以将等于 val 的值都移到最后一位
                nums[slow],nums[fast] = nums[fast],nums[slow]
                slow += 1
                fast += 1
        return slow

if __name__ == '__main__':
    s = Solution()
    print(s.removeElement([2,3,3,2],3))

# 方法2
class Solution:
    def removeVal(self,nums: List[int],val):
        sum = 0 # 代表数组的下标
        n = len(nums)
        for i in range(n):
            # 当nums[i] 与 val 不相等时,将nums[i] 与 nums[sum]交换位置,达到将等于 val 的值都移到列表后面,前面都是不等于 val 的值
            if nums[i] != val:
                nums[sum],nums[i] = nums[i],nums[sum]
                sum += 1
        return sum


if __name__ == '__main__':
    s = Solution()
    print(s.removeVal([0,1,2,2,3,0,4,2],2))