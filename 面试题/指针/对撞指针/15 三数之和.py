"""
:Author: Mr.Liu
:Create: 2020/6/28 10:36
:Github: https://XXXXXXXX
Copyright (c) 2020,Mr.Liu Group All Rights Reserved.
"""

"""给你一个包含 n 个整数的数组 nums，判断 nums 中是否存在三个元素 a，b，c ，使得 a + b + c = 0 ？请你找出所有满足条件且不重复的三元组。
注意：答案中不可以包含重复的三元组。
示例：
给定数组 nums = [-1, 0, 1, 2, -1, -4]，
满足要求的三元组集合为：
[[-1, 0, 1],[-1, -1, 2]]
"""

from typing import List
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort() # 排序
        res = []  # 用来保存最后输出的值
        for i in range(len(nums)-2):
            if i > 0 and nums[i] == nums[i-1]: # 去重
                continue
            left = i + 1 # 首指针
            right = len(nums)-1 # 尾指针
            while left < right:
                if nums[left] +nums[right] + nums[i] > 0:
                    right -= 1
                elif nums[left] + nums[right] + nums[i] < 0:
                    left += 1
                else:
                    res.append([nums[i],nums[left],nums[right]])
                    while left < right and nums[left] == nums[left+1]: # 去重
                        left += 1
                    while left < right and nums[right] == nums[right-1]: # 去重
                        right -= 1
                    left += 1
                    right -= 1
        return res
if __name__ == '__main__':
    s = Solution()
    print(s.threeSum([-1,0,1,2,-1,-4]))



