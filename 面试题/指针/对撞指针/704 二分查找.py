"""
:Author: Mr.Liu
:Create: 2020/6/26 15:24
:Github: https://XXXXXXXX
Copyright (c) 2020,Mr.Liu Group All Rights Reserved.
"""
"""给定一个 n 个元素有序的（升序）整型数组 nums 和一个目标值 target  ，写一个函数搜索 nums 中的 target，如果目标值存在返回下标，否则返回 -1。

示例 1:
    输入: nums = [-1,0,3,5,9,12], target = 9
    输出: 4
    解释: 9 出现在 nums 中并且下标为 4
示例 2:
    输入: nums = [-1,0,3,5,9,12], target = 2
    输出: -1
    解释: 2 不存在 nums 中因此返回 -1
来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/binary-search
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

# 方法1
from typing import List
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0 # 首指针
        right = len(nums) - 1 # 尾指针
        while left <= right:
            if target not in nums: # 当查找对应的值不存在与数组中,返回 -1
                return -1
            if nums[left] == target:
                return left
            elif nums[right] == target:
                return right
            else:
                mid = (left + right) // 2 # 中间下标
                if target < nums[mid]:
                    right = mid
                elif target > nums[mid]:
                    left = mid
                else:
                    return mid
if __name__ == '__main__':
    s = Solution()
    print(s.search([-1,0,3,5,9,12],2))

# 方法2
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = -1 # 首指针
        right = len(nums) # 尾指针
        while left <= right:
            if target not in nums:
                return -1
            mid = (left + right) // 2 # 中间下标
            if target < nums[mid]:
                right = mid
            elif target > nums[mid]:
                left = mid
            else:
                return mid

if __name__ == '__main__':
    s = Solution()
    print(s.search([-1,0,3,5,9,12],2))

# 方法3
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = -1 # 首指针
        right = len(nums) # 尾指针
        while left <= right:
            if target not in nums:
                return -1
            mid = left + (right - left) // 2  # 其他语言方法都适用,防止数值溢出,超出范围,导致出错
            if target < nums[mid]:
                right = mid
            elif target > nums[mid]:
                left = mid
            else:
                return mid

if __name__ == '__main__':
    s = Solution()
    print(s.search([-1,0,3,5,9,12],2))

# 方法4
# 递归版
def search(nums: List[int], target: int,left:int,right:int) -> int:
    if right > 0:
        mid = left + (right - left) // 2 # 中间下标
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            return search(nums,target,mid + 1,right)
        else:
            return search(nums, target,left,mid - 1)
    else:
        return -1

a = list(range(30))
target = 10
print(search(a,target,-1,30))