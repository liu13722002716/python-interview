"""
:Author: Mr.Liu
:Create: 2020/6/23 16:14
:Github: https://XXXXXXXX
Copyright (c) 2020,Mr.Liu Group All Rights Reserved.
"""
"""给定一个整数数组 nums 和一个目标值 target，请你在该数组中找出和为目标值的那 两个 整数，并返回他们的数组下标。
你可以假设每种输入只会对应一个答案。但是，数组中同一个元素不能使用两遍。

示例
给定 nums = [2, 7, 11, 15], target = 9
因为 nums[0] + nums[1] = 2 + 7 = 9
所以返回 [0, 1]
"""

# 方法1
from typing import List
class Solution:
    def twoSum(self, nums: List[int], target: int):
        n1 = nums[:] # 将 nums 的值保存到 n1 中
        n2 = n1[::-1] # 将 nums 原来的值进行倒序,为了后面使用index方法的缺陷使用
        nums.sort() # 排序
        left = 0 # 首指针
        right = len(nums) - 1 # 尾指针
        while left < right:
            curr = nums[left] + nums[right]
            if curr == target:
                left = nums[left]
                right = nums[right]
                break
            else:
                if curr < target:
                    left += 1
                else:
                    right -= 1
        x = n1.index(left)  # 根据对撞指针获取的数值来求出对应的下标
        y = (len(n2) - 1) - n2.index(right)
        if x < y:  # 判断下标的大小,保证输出的小标是有序的
            return [x, y]
        else:
            return [y, x]

if __name__ == '__main__':
    s = Solution()
    print(s.twoSum([3,2,4],6))

# 方法2
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)): # 外循环
            for j in range(i+1,len(nums)): # 内循环
                if nums[i] + nums[j] == target:
                    return [i,j]
        return False

if __name__ == '__main__':
    s = Solution()
    print(s.twoSum([3,2,4],6))

# 方法3
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_dict = {} # 空的字典
        for i in range(len(nums)):
            temp = target - nums[i]  # 计算差值
            if temp in nums_dict: # 当差值存在字典中输出对应下标
                return [i,nums_dict[temp]]
            else: # 当差值不存在字典中,将数值作为 key ,下标作为 value 加入字典中,方便查找;
                nums_dict[nums[i]] = i
if __name__ == '__main__':
    s = Solution()
    print(s.twoSum([2,7,11,15],9))


